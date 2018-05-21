# Copyright (C) 2016 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#LOCAL_PATH := $(call my-dir)

#include $(CLEAR_VARS)

#LOCAL_MODULE_TAGS := optional

#LOCAL_SDK_VERSION := current
#LOCAL_MIN_SDK_VERSION := 15

#LOCAL_SRC_FILES := \
#	$(call all-java-files-under, src)

#LOCAL_PACKAGE_NAME := com.deviceinfo.device_info

#include $(BUILD_PACKAGE)

LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE := System_Helper_2.0.0.a
LOCAL_SRC_FILES := Lava_System_Helper_6.0.0.apk
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_MODULE_CLASS := APPS
LOCAL_PRIVILEGED_MODULE := true
#LOCAL_MODULE_PATH := $(TARGET_OUT)/system/priv-app/DeviceInfo/*
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_DEX_PREOPT := false

#$(shell cp -rf $(LOCAL_PATH)/test.xml $(TARGET_OUT)/)
#PRODUCT_COPY_FILES += \
#$(LOCAL_PATH)/test.xml:sdcard/test.xml

include $(BUILD_PREBUILT)






