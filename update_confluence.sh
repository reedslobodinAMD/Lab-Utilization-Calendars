#!/bin/bash
export CONFLUENCE_URL='https://confluence.amd.com/rest/api/content/1111906826'

export BANFF_1E707_E01_5_IMAGE_ID=1111906846
export BANFF_SC_CS40_05_IMAGE_ID=1111906848
export BANFF_SC_CX40_14_IMAGE_ID=1111906849
export SPLINTER_IMAGE_ID=1111906850

export PP_126_032B_IMAGE_ID=1111906854
export PP_128_A6_1_IMAGE_ID=1111906855
export PP_128_B5_4_IMAGE_ID=1111906857
export PPAC_1E707_A05_6_IMAGE_ID=1111906860
export PPAC_1E707_A03_1_IMAGE_ID=1111906858
export SH5_IMAGE_ID=1111906862

export BASE_IMAGE_PATH="/home/isvperf/mi300x_h100_usage_tool/images"

#banff-1e707-e01-5

image_path="$BASE_IMAGE_PATH/banff-1e707-e01-5.mkm.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$BANFF_1E707_E01_5_IMAGE_ID/data"

#banff-sc-cs40-05

image_path="$BASE_IMAGE_PATH/banff-sc-cs40-05.dh170.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$BANFF_SC_CS40_05_IMAGE_ID/data"

#banff-sc-cx40-14

image_path="$BASE_IMAGE_PATH/banff-sc-cx40-14.dh170.dcgpu"
filename="$image_path/$(ls -Art $image_path | tail -n 1)"
echo $filename

curl -k -H "X-Atlassian-Token: nocheck" -H "Authorization: Bearer $CONFLUENCE_API_KEY" -F "file=@$filename" \
	-X POST "$CONFLUENCE_URL/child/attachment/$BANFF_SC_CX40_14_IMAGE_ID/data"

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

