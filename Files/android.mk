LOCAL_PATH := $(call my-dir) include
$(CLEAR_VARS) LOCAL_MODULE
:= DeviceInfo
LOCAL_SRC_FILES := K2konnect_FOTA_7.0.8_F.apk
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_MODULE_CLASS := APPS
LOCAL_PRIVILEGED_MODULE := true
LOCAL_CERTIFICATE := platform
LOCAL_DEX_PREOPT := false include
$(BUILD_PREBUILT)
