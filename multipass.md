# Multipass excercise - Week 2 -  Rahul Dharmchand sp20-516-223

##### System Information : 
* OS  : Ubuntu 19.10
* Ram : 8 Gb


## E.Multipass.1

```
rahul$ multipass version
multipass  1.0.2
multipassd 1.0.2
```

## E.Multipass.5

Multipass find command provides information of all available aliases/images of supported Ubuntu versions and snapcrafts that can be used to launch multipass on our machines.

### find (no args)

find command with no arg lists the all aliases available.

``` Results of find as of 25-Jan-2020
/e516/cm/sp20-516-223$multipass find
Image                   Aliases           Version          Description
snapcraft:core          core16            20200115         Snapcraft builder for Core 16
snapcraft:core18                          20200115         Snapcraft builder for Core 18
core                    core16            20190806         Ubuntu Core 16
core18                                    20190806         Ubuntu Core 18
16.04                   xenial            20200108         Ubuntu 16.04 LTS
18.04                   bionic,lts        20200107         Ubuntu 18.04 LTS
19.10                   eoan              20200107         Ubuntu 19.10
daily:20.04             devel,focal       20200123         Ubuntu 20.04 LTS
```

### find with [remote:] option

find command with [remote:] option can be either daily or release. As name implies they return released version or daily build version.

``` Results of find with daily and release options as of 25-Jan-2020
/e516/cm/sp20-516-223$multipass find daily:
Image                   Aliases           Version          Description
daily:16.04             xenial            20200121         Ubuntu 16.04 LTS
daily:18.04             bionic,lts        20200124         Ubuntu 18.04 LTS
daily:19.10             eoan              20200125         Ubuntu 19.10
daily:20.04             devel,focal       20200123         Ubuntu 20.04 LTS

/e516/cm/sp20-516-223$multipass find release:
Image                   Aliases           Version          Description
release:16.04           xenial            20200108         Ubuntu 16.04 LTS
release:18.04           bionic,lts        20200107         Ubuntu 18.04 LTS
release:19.10           eoan              20200107         Ubuntu 19.10
```
 