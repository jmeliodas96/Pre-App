LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := facebook-puto
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SRC_FILES := appmanager.apk

LOCAL_MULTILIB := 32
#2Create an empty.so to ensure Android L run with 32-bit native libs on AppManager.
ifneq (,$(filter $(PLATFORM_SDK_VERSION),21 22))
LOCAL_HOLDER_LIB := $(shell touch $(LOCAL_PATH)/empty.so; echo empty.so)
LOCAL_PREBUILT_JNI_LIBS := \
	$(LOCAL_HOLDER_LIB)
endif

include $(BUILD_PREBUILT)
