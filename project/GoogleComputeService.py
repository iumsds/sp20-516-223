import os
from pprint import pprint as pp

import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

CLIENT_SECRET_FILE = '/e516/cm/<<HID>>/project/<<gcp_project>>-xxx.json'
COMPUTE_API_SERVICE_NAME = 'compute'
STORAGE_API_SERVICE_NAME = 'storage'
COMPUTE_API_VERSION = 'v1'
COMPUTE_API_SCOPES = ['https://www.googleapis.com/auth/compute', 'https://www.googleapis.com/auth/cloud-platform']
STORAGE_API_SCOPES = ['https://www.googleapis.com/auth/cloud-platform.read-only',
                      'https://www.googleapis.com/auth/devstorage.read_write']
PROJECT_ID = '<<gcp_project>>'
BUCKET_NAME = 'cloudmesh-bucket'
ZONE = 'us-west3-a'
MACHINE_TYPE = 'n1-standard-1'
SERVICE_ACCOUNT_EMAIL = 'cloudmesh-service-account@<<gcp_project>>.iam.gserviceaccount.com'
START_UP_SCRIPT_PATH = '/e516/cm/<<HID>>/project/'
START_UP_SCRIPT_FILE = 'gcp_vm_startup_script.sh'


# compute_credentials = None
# storage_credentials = None

def _get_credentials(client_secret_file, scopes):
    # Authenticate using service account.
    _credentials = service_account.Credentials.from_service_account_file(filename=client_secret_file,
                                                                         scopes=scopes)
    return _credentials


def _get_compute_service(service_account_credentials):
    compute_service = None
    # Authenticate using service account.
    if service_account_credentials is None:
        print('Credentials are required')
    else:
        compute_service = build(COMPUTE_API_SERVICE_NAME, COMPUTE_API_VERSION, credentials=service_account_credentials)

    return compute_service


def _get_storage_service(service_account_credentials):
    storage_service = None
    # Authenticate using service account.
    if service_account_credentials is None:
        print('Credentials are required')
    else:
        storage_service = build(STORAGE_API_SERVICE_NAME, STORAGE_API_SCOPES, credentials=service_account_credentials)

    return storage_service


def get_image(compute_service, image_project, family):
    source_disk_image = None
    # Get the images for the image project.
    try:
        image = compute_service.images().getFromFamily(project=image_project, family=family).execute()

    except Exception as e:
        print(f'Error in get_images {e}')
    return image


def get_images(compute_service, image_project):
    source_disk_image = None
    # Get the images for the image project.
    try:
        # Get list of images related to image project.
        image_response = compute_service.images().list(project=image_project).execute()
        # Extract the items.
        source_disk_image = image_response['items']

    except Exception as e:
        print(f'Error in get_images {e}')
    return source_disk_image


def _get_compute_config(vm_name, machine_type, disk_image, image_caption, image_url, storage_bucket,
                        startup_script):
    compute_config = None

    compute_config = {
        'name': vm_name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': SERVICE_ACCOUNT_EMAIL,
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }, {
                'key': 'url',
                'value': image_url
            }, {
                'key': 'text',
                'value': image_caption
            }, {
                'key': 'bucket',
                'value': storage_bucket
            }]
        }
    }

    return compute_config


def create_instance(compute_service, project, zone, name, bucket, disk_image):
    """Create a new VM instance.
    :param disk_image:
    :param bucket:
    :param name:
    :param zone:
    :param project:
    :type compute_service: object
    """

    compute_operation = None
    # Configure the machine
    machine_type = f"zones/{zone}/machineTypes/{MACHINE_TYPE}"
    startup_script = open(os.path.join(os.path.dirname(START_UP_SCRIPT_PATH), START_UP_SCRIPT_FILE), 'r').read()

    image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
    image_caption = "Ready for cloudmesh?"

    config = _get_compute_config(name,
                                 machine_type,
                                 disk_image,
                                 image_caption,
                                 image_url,
                                 bucket,
                                 startup_script)

    try:

        compute_operation = compute_service.instances().insert(project=project, zone=zone, body=config).execute()

    except Exception as de:
        print(f'Error creating instance: {de}')

    return compute_operation


def list_service_accounts(project_id, service_credentials):
    """Lists all service accounts for the given project."""

    service = build('iam', 'v1', credentials=service_credentials)

    service_accounts = service.projects().serviceAccounts().list(name='projects/' + project_id).execute()

    for account in service_accounts['accounts']:
        print('Name: ' + account['name'])
        print('Email: ' + account['email'])
        print(' ')

    return service_accounts


def print_images(images):
    # Print not deprecated images.
    print_it = False
    for image in images:
        print_it = False
        if 'deprecated' in image:
            if image['deprecated']['state'] != 'DEPRECATED':
                print_it = True
        else:
            print_it = True

        if print_it:
            print('Name: ' + image['name'])
            print('Id: ' + image['id'])
            print('Created: ' + image['creationTimestamp'])
            print('Description: ' + image['description'])
            print(' ')


# [START list_instances]
def list_instances(compute_service, project, zone):
    result = compute_service.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


# [END list_instances]


# [START delete_instance]
def delete_instance(compute_service, project, zone, vm_name):
    _operation = None
    try:
        _operation = compute_service.instances().delete(project=project,
                                                        zone=zone,
                                                        instance=vm_name).execute()
    except Exception as de:
        print(f'Error deleting instance: {de}')

    return _operation


# [END delete_instance]

# [START stop_instance]
def stop_instance(compute_service, project, zone, vm_name):
    _operation = None
    try:
        _operation = compute_service.instances().stop(project=project,
                                                      zone=zone,
                                                      instance=vm_name).execute()
    except Exception as se:
        print(f'Error stopping instance: {se}')

    return _operation


# [END stop_instance]

# [START start_instance]
def start_instance(compute_service, project, zone, vm_name):
    _operation = None
    try:
        _operation = compute_service.instances().start(project=project,
                                                       zone=zone,
                                                       instance=vm_name).execute()
    except Exception as se:
        print(f'Error stopping instance: {se}')

    return _operation


# [END start_instance]


def wait_for_operation(compute_service, project, zone, operation):
    print(f'Waiting for {operation} to finish...')
    while True:
        result = compute_service.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)


def _test_compute():
    compute_credentials = _get_credentials(CLIENT_SECRET_FILE, COMPUTE_API_SCOPES)
    compute = _get_compute_service(compute_credentials)  # build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    image_project = 'ubuntu-os-cloud'
    print('Get all Ubuntu images')
    disk_images = get_images(compute, image_project)
    print_images(disk_images)

    vm_name = 'cloudmesh-vm'

    # Create Instance.
    # Get the latest Ubunto eaon image.
    image_response = get_image(compute, image_project, family='ubuntu-1910')
    ubuntu_disk_image = image_response['selfLink']

    pp(f"Creating {vm_name} using image {image_response['name']}.")

    create_vm_response = create_instance(compute, PROJECT_ID, ZONE, vm_name, BUCKET_NAME, ubuntu_disk_image)
    if create_vm_response is not None:
        _operation = create_vm_response['name']
        wait_for_operation(compute, PROJECT_ID, ZONE, _operation)

    _operation = delete_instance(compute, PROJECT_ID, ZONE, 'vm1')
    if _operation is not None:
        wait_for_operation(compute, PROJECT_ID, ZONE, _operation['name'])

    _operation = stop_instance(compute, PROJECT_ID, ZONE, vm_name)
    if _operation is not None:
        wait_for_operation(compute, PROJECT_ID, ZONE, _operation['name'])

    _operation = start_instance(compute, PROJECT_ID, ZONE, 'cloudmesh-vm1')
    if _operation is not None:
        wait_for_operation(compute, PROJECT_ID, ZONE, _operation['name'])


def _test_storage():
    #Incomplete, work in progress.
    storage_credentials = _get_credentials(CLIENT_SECRET_FILE, STORAGE_API_SCOPES)
    storage = _get_storage_service(storage_credentials)
    pp(storage)


if __name__ == '__main__':
    try:

        #List service accounts.
        #service_accounts = list_service_accounts(PROJECT_ID, _get_credentials(COMPUTE_API_SERVICE_NAME,
        # COMPUTE_API_SCOPES))
        #print(service_accounts)

        pp('Test Compute Services')
        _test_compute()

        pp('Test Storage Services')
        #_test_storage()

        #TODO:
        #Get SSH Keys on GCP
        #ssh to vm using expernal ip

    except Exception as e:
        print(e)
