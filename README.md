# Halo Vulnerability Report

Version: *1.0*
<br />
Author: *Sean Nicholson*


### Halo API Key
Place the values inside of cloudpassage.yml. The key_id and secret_key can be found from the Halo portal under Site Admin -> Api keys. This script requires an API key with write permission to run.

```
    key_id:
    secret_key:
    api_hostname : https://api.cloudpassage.com
    cve_url: https://cve.mitre.org/cgi-bin/cvename.cgi?name=
```

### Prerequisities

1. cloudpassage sdk (Can be installed here: https://github.com/cloudpassage/cloudpassage-halo-python-sdk/tree/develop or "pip install cloudpassage")

2. Populate the following values in cloudpassage.yml

  * key_id, secret_key pair (This is your halo portal api_keys)

### Dependencies

  1. Python 2.7.10 or newer Python 2.7.x
  2. cloudpassage python package (pip install cloudpassage)


### Run
Script will cycle through the all open issues in the API Key scope and resolve them.
To resolve all issues for a particular group, use an API key with the scope of that group.
To resolve all issues for a portal, use a root group scope API Key.

Depending on the number of issues in your portal, you may have to run this script multiple times.

```
    python resolve_all_issues.py
```

### Customizing which issues are resolved
To resolve only issues from one module change line 23 of the resolve_all_issues.py
For this example, this change would resolve only SAM issues for the scope of the API key.
>Change from
    list_of_issues_json = issues.get_paginated("/v2/issues", 'issues', 10)
Change To
    list_of_issues_json = issues.get_paginated("/v2/issues?issue_type=sam", 'issues', 10)

Issues endpoint type examples: lids, fim, csm, sva, sam



## License

Copyright (c) 2017, CloudPassage, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the CloudPassage, Inc. nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL CLOUDPASSAGE, INC. BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED ANDON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
