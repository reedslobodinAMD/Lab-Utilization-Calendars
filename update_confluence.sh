#!/bin/bash
export CONFLUENCE_URL='https://confluence.amd.com/rest/api/content/1111906826'

export BANFF_1E707_E05_5_IMAGE_ID=1165846081
export BANFF_1E707_C01_1_IMAGE_ID=1206304371
export BANFF_PLA_U29_29_IMAGE_ID=1206304301
export SPLINTER_IMAGE_ID=1218808962

export PP_126_032B_IMAGE_ID=1206304280
export PP_128_A6_1_IMAGE_ID=1218808998
export PP_128_B5_4_IMAGE_ID=1206304287
export PPAC_1E707_A05_6_IMAGE_ID=1206304293
export PPAC_1E707_A03_1_IMAGE_ID=1206304291
export SH5_IMAGE_ID=1206304295

export GPUPERF_LAB_72_IMAGE_ID=1206304364
export GPUPERF_LAB_73_IMAGE_ID=1206304367

export GPUPERF_LAB_79_IMAGE_ID=1190592488
export GPUPERF_LAB_80_IMAGE_ID=1190592490
export GPUPERF_LAB_81_IMAGE_ID=1190592494
export GPUPERF_LAB_82_IMAGE_ID=1190592496

export BASE_IMAGE_PATH="/home/isvperf/mi300x_h100_usage_tool/images"

#banff-1e707-e05-5

image_path="$BASE_IMAGE_PATH/banff-1e707-e05-5.mkm.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$BANFF_1E707_E05_5_IMAGE_ID/data"


#banff-1e707-c01-1

image_path="$BASE_IMAGE_PATH/banff-1e707-c01-1.mkm.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$BANFF_1E707_C01_1_IMAGE_ID/data"


#banff-pla-u29-29

image_path="$BASE_IMAGE_PATH/banff-pla-u29-29.pla.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
        -X POST "$CONFLUENCE_URL/child/attachment/$BANFF_PLA_U29_29_IMAGE_ID/data"


#splinter-1w300-f0-2a

image_path="$BASE_IMAGE_PATH/splinter-1w300-f0-2a.mkm.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$SPLINTER_IMAGE_ID/data"


#pp-126-032b

image_path="$BASE_IMAGE_PATH/pp-126-032b.aus.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$PP_126_032B_IMAGE_ID/data"

#pp-128-a6-1

image_path="$BASE_IMAGE_PATH/pp-128-a6-1.aus.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$PP_128_A6_1_IMAGE_ID/data"

#pp-128-b5-4

image_path="$BASE_IMAGE_PATH/pp-128-b5-4.aus.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$PP_128_B5_4_IMAGE_ID/data"

#ppac-1e707-a05-6

image_path="$BASE_IMAGE_PATH/ppac-1e707-a05-6.mkm.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$PPAC_1E707_A05_6_IMAGE_ID/data"

#ppac-1e707-a03-1

image_path="$BASE_IMAGE_PATH/ppac-1e707-a03-1.mkm.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$PPAC_1E707_A03_1_IMAGE_ID/data"

#sh5-126-b3-1

image_path="$BASE_IMAGE_PATH/sh5-126-b3-1.aus.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$SH5_IMAGE_ID/data"

#gpuperf-lab-72

image_path="$BASE_IMAGE_PATH/gpuperf-lab-72.gpuperf"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$GPUPERF_LAB_72_IMAGE_ID/data"

#gpuperf-lab-73

image_path="$BASE_IMAGE_PATH/gpuperf-lab-73.gpuperf"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$GPUPERF_LAB_73_IMAGE_ID/data"


#gpuperf-lab-79

image_path="$BASE_IMAGE_PATH/gpuperf-lab-79.gpuperf"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$GPUPERF_LAB_79_IMAGE_ID/data"


#gpuperf-lab-80

image_path="$BASE_IMAGE_PATH/gpuperf-lab-80.gpuperf"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$GPUPERF_LAB_80_IMAGE_ID/data"


#gpuperf-lab-81

image_path="$BASE_IMAGE_PATH/gpuperf-lab-81.gpuperf"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$GPUPERF_LAB_81_IMAGE_ID/data"


#gpuperf-lab-82

image_path="$BASE_IMAGE_PATH/gpuperf-lab-82.gpuperf"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$GPUPERF_LAB_82_IMAGE_ID/data"
