# dstack  
  
### follow the steps below to set up dstack and run a simple test workflow  
  
```
> pip install dstack  
```
  
 if you use a private repo (not this case) you need  
 to authorize dstack  
  
```
> dstack init [-t GITHUB_TOKEN | -i SSH_PRIVATE_KEY]  
```
  
```
> mkdir dstack_test  
> cd dstack_test  
> git clone https://github.com/eafpres/dstack.git  
> cd dstack  
> dstack config  
```
  
 note that dstack uses the .aws credentials on your computer  
 these are in ~/.aws/credentials or c:/users/<your user> /.aws/credentials  
 a sample file is provided in the repo  
  
> ...   
  
 dstack prompts you for AWS region, AWS S3 bucket name,   
 optional AWS credentials, optional AWS region subnet  
  
 do not use a generic bucket name like dstack-test as AWS looks globally  
 and will not allow you to use a bucket already in use anywhwere else  
 unless you have permission  
 dstack-test for example IS in use and you will fail the configure   
 and it can be confusing!  
 use something unique to your account  
 also note that if you use an existing bucket, it must be in the same region  
 as you specify in the config  
  
 dstack can use tags to refer to assets making it easy  
 to incorporate them into workflows  
 in this example, the workflow expects a tag test-dstack-data  
 to refer to the data directory in the cloned repo  
 here you add the tag to the repo just configured  
  
```
> dstack tags add test-dstack-data -a ./data  
```
  
 in the cloned repo in the .dstack folder  
 is a workflows .yaml file with a named workflow  
  
```
> dstack run read_data  
  
> ...  
```
 dstack spins up an AWS EC2, configures it using the requirements.txt  
 then runs the rest of the workflow, in this case running   
 the python script from the code directory  
 this script reads a .csv file  
 prints a summary  
 saves the summary to a new .csv file  
 and saves a plot to a .jpg file  
  
 you should see something similar to this in the console  
  
```
> (python38) PS C:\dstack_test\dstack>  dstack run read_data  
>  RUN      WORKFLOW      STATUS   APPS  ARTIFACTS       SUBMITTED   TAG  
>  hard-puma-1  read_data     Submitted    output        55 sec ago  
>   
> Provisioning... It may take up to a minute. ✓  
>   
> To interrupt, press Ctrl+C.  
>   
> Collecting pandas==1.3.4  
>   Downloading pandas-1.3.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.5 MB)  
> Collecting matplotlib==3.5.0  
>   Downloading matplotlib-3.5.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (11.3 MB)  
> Collecting numpy> =1.17.3  
>   Downloading numpy-1.23.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1 MB)  
> Collecting pytz> =2017.3  
>   Downloading pytz-2022.4-py2.py3-none-any.whl (500 kB)  
> Collecting python-dateutil> =2.7.3  
>   Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)  
> Collecting cycler> =0.10  
>   Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)  
> Collecting setuptools-scm> =4  
>   Downloading setuptools_scm-7.0.5-py3-none-any.whl (42 kB)  
> Collecting pillow> =6.2.0  
>   Downloading Pillow-9.2.0-cp38-cp38-manylinux_2_28_x86_64.whl (3.2 MB)  
> Collecting pyparsing> =2.2.1  
>   Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)  
> Collecting kiwisolver> =1.0.1  
>   Downloading kiwisolver-1.4.4-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)  
> Collecting fonttools> =4.22.0  
>   Downloading fonttools-4.37.4-py3-none-any.whl (960 kB)  
> Collecting packaging> =20.0  
>   Downloading packaging-21.3-py3-none-any.whl (40 kB)  
> Requirement already satisfied: six> =1.5 in /opt/conda/lib/python3.8/site-packages (from python-dateutil> =2.7.3-> pandas==1.3.4-> -r requirements.txt (line 1)) (1.16.0)  
> Requirement already satisfied: setuptools in /opt/conda/lib/python3.8/site-packages (from setuptools-scm> =4-> matplotlib==3.5.0-> -r requirements.txt (line 2)) (61.2.0)  
> Collecting typing-extensions  
>   Downloading typing_extensions-4.4.0-py3-none-any.whl (26 kB)  
> Collecting tomli> =1.0.0  
>   Downloading tomli-2.0.1-py3-none-any.whl (12 kB)  
> Installing collected packages: pyparsing, typing-extensions, tomli, packaging, setuptools-scm, pytz, python-dateutil, pillow, numpy, kiwisolver, fonttools, cycler, pandas, matplotlib  
> Successfully installed cycler-0.11.0 fonttools-4.37.4 kiwisolver-1.4.4 matplotlib-3.5.0 numpy-1.23.4 packaging-21.3 pandas-1.3.4 pillow-9.2.0 pyparsing-3.0.9 python-dateutil-2.8.2 pytz-2022.4 setuptools-scm-7.0.5 tomli-2.0.1 typing-extensions-4.4.0  
```
  
```
> found OS  linux  
> user is:  None  
> working directory is:  /workflow  
> data summary  
>          x      y  
> count  76.000000  76.000000  
> mean   38.500000  1974.026316  
> std  22.083176  1754.755717  
> min   1.000000  11.000000  
> 25%  19.750000   401.000000  
> 50%  38.500000  1493.000000  
> 75%  57.250000  3288.750000  
> max  76.000000  5787.000000  
```
  
 after completion, you can inspect the bucket and   
 within the path bucket/artifacts/user/repo/run/output  
 and see the files created  
 note that here bucket is the bucket name you specified  
 artifacts folder is created by dstack  
 user is the AWS profile name  
 repo is the name of the repo (in this case, dstack)  
 run is the run-name assigned by dstack (hard-puma-1 in this case)  
 output folder is created by the code  
  
 you can also see artifacts from the CLI  
  
```
> dstack list artifiacts hard-puma-1  
>  ARTIFACT  FILE              SIZE  
>  output    data_summary.csv  170.0B  
>            parabolic.jpg     29.3KiB  
```