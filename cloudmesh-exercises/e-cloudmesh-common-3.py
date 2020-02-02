# fa20-516-223 E.Cloudmesh.Common.3

from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE

dist = Shell.distribution()

rahul_dist = {"name": "rahul",
              "dist": dist}

VERBOSE(rahul_dist)

# Convert the dict to flat distribution.
flatdist = FlatDict(rahul_dist, sep=".")

print(flatdist["dist.platform"])
