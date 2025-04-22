from anixart.utils import endpoint

# # ----------- # RELEASE # ----------- #
# # TODO PROFILE: SETTINGS, SETTINGS_RELEASE, SETTINGS_RELEASE_FIRST,
# #  SETTINGS_COMMENTS, SETTINGS_COLLECTION, EDIT_AVATAR, SETTINGS_RELEASE_LIST,
# #  SETTINGS_RELEASE_TYPE
#
# # GET
#
#
#
# # POST
#
#
#

class AnixartProfileEndpoints:
    release = endpoint("/release/{id}", "GET", None, {"id": int}, {})
