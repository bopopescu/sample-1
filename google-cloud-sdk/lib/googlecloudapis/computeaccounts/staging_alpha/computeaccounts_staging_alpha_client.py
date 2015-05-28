"""Generated client library for computeaccounts version staging_alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudapis.apitools.base.py import base_api
from googlecloudapis.computeaccounts.staging_alpha import computeaccounts_staging_alpha_messages as messages


class ComputeaccountsStagingAlpha(base_api.BaseApiClient):
  """Generated client library for service computeaccounts version staging_alpha."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'computeaccounts'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/computeaccounts', u'https://www.googleapis.com/auth/computeaccounts.readonly']
  _VERSION = u'staging_alpha'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = ''
  _CLIENT_CLASS_NAME = u'ComputeaccountsStagingAlpha'
  _URL_VERSION = u'staging_alpha'

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new computeaccounts handle."""
    url = url or u'https://www.googleapis.com/computeaccounts/staging_alpha/'
    super(ComputeaccountsStagingAlpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.globalAccountsOperations = self.GlobalAccountsOperationsService(self)
    self.groups = self.GroupsService(self)
    self.linux = self.LinuxService(self)
    self.users = self.UsersService(self)

  class GlobalAccountsOperationsService(base_api.BaseApiService):
    """Service class for the globalAccountsOperations resource."""

    _NAME = u'globalAccountsOperations'

    def __init__(self, client):
      super(ComputeaccountsStagingAlpha.GlobalAccountsOperationsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'computeaccounts.globalAccountsOperations.delete',
              ordered_params=[u'project', u'operation'],
              path_params=[u'operation', u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/operations/{operation}',
              request_field='',
              request_type_name=u'ComputeaccountsGlobalAccountsOperationsDeleteRequest',
              response_type_name=u'ComputeaccountsGlobalAccountsOperationsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'computeaccounts.globalAccountsOperations.get',
              ordered_params=[u'project', u'operation'],
              path_params=[u'operation', u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/operations/{operation}',
              request_field='',
              request_type_name=u'ComputeaccountsGlobalAccountsOperationsGetRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'computeaccounts.globalAccountsOperations.list',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[u'filter', u'maxResults', u'pageToken'],
              relative_path=u'projects/{project}/global/operations',
              request_field='',
              request_type_name=u'ComputeaccountsGlobalAccountsOperationsListRequest',
              response_type_name=u'OperationList',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the specified operation resource.

      Args:
        request: (ComputeaccountsGlobalAccountsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ComputeaccountsGlobalAccountsOperationsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Retrieves the specified operation resource.

      Args:
        request: (ComputeaccountsGlobalAccountsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves the list of operation resources contained within the specified project.

      Args:
        request: (ComputeaccountsGlobalAccountsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OperationList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class GroupsService(base_api.BaseApiService):
    """Service class for the groups resource."""

    _NAME = u'groups'

    def __init__(self, client):
      super(ComputeaccountsStagingAlpha.GroupsService, self).__init__(client)
      self._method_configs = {
          'AddMember': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.groups.addMember',
              ordered_params=[u'project', u'groupName'],
              path_params=[u'groupName', u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/groups/{groupName}/addMember',
              request_field=u'groupsAddMemberRequest',
              request_type_name=u'ComputeaccountsGroupsAddMemberRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'computeaccounts.groups.delete',
              ordered_params=[u'project', u'groupName'],
              path_params=[u'groupName', u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/groups/{groupName}',
              request_field='',
              request_type_name=u'ComputeaccountsGroupsDeleteRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'computeaccounts.groups.get',
              ordered_params=[u'project', u'groupName'],
              path_params=[u'groupName', u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/groups/{groupName}',
              request_field='',
              request_type_name=u'ComputeaccountsGroupsGetRequest',
              response_type_name=u'Group',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.groups.insert',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/groups',
              request_field=u'group',
              request_type_name=u'ComputeaccountsGroupsInsertRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'computeaccounts.groups.list',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[u'filter', u'maxResults', u'pageToken'],
              relative_path=u'projects/{project}/global/groups',
              request_field='',
              request_type_name=u'ComputeaccountsGroupsListRequest',
              response_type_name=u'GroupList',
              supports_download=False,
          ),
          'RemoveMember': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.groups.removeMember',
              ordered_params=[u'project', u'groupName'],
              path_params=[u'groupName', u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/groups/{groupName}/removeMember',
              request_field=u'groupsRemoveMemberRequest',
              request_type_name=u'ComputeaccountsGroupsRemoveMemberRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def AddMember(self, request, global_params=None):
      """Adds users to the specified group.

      Args:
        request: (ComputeaccountsGroupsAddMemberRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddMember')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the specified Group resource.

      Args:
        request: (ComputeaccountsGroupsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the specified Group resource.

      Args:
        request: (ComputeaccountsGroupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Group) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a Group resource in the specified project using the data included in the request.

      Args:
        request: (ComputeaccountsGroupsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves the list of groups contained within the specified project.

      Args:
        request: (ComputeaccountsGroupsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GroupList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def RemoveMember(self, request, global_params=None):
      """Removes users from the specified group.

      Args:
        request: (ComputeaccountsGroupsRemoveMemberRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('RemoveMember')
      return self._RunMethod(
          config, request, global_params=global_params)

  class LinuxService(base_api.BaseApiService):
    """Service class for the linux resource."""

    _NAME = u'linux'

    def __init__(self, client):
      super(ComputeaccountsStagingAlpha.LinuxService, self).__init__(client)
      self._method_configs = {
          'GetAuthorizedKeysView': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.linux.getAuthorizedKeysView',
              ordered_params=[u'project', u'zone', u'user', u'instance'],
              path_params=[u'project', u'user', u'zone'],
              query_params=[u'instance'],
              relative_path=u'projects/{project}/zones/{zone}/authorizedKeysView/{user}',
              request_field='',
              request_type_name=u'ComputeaccountsLinuxGetAuthorizedKeysViewRequest',
              response_type_name=u'LinuxGetAuthorizedKeysViewResponse',
              supports_download=False,
          ),
          'GetLinuxAccountViews': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.linux.getLinuxAccountViews',
              ordered_params=[u'project', u'zone', u'instance'],
              path_params=[u'project', u'zone'],
              query_params=[u'filter', u'instance', u'maxResults', u'pageToken', u'user'],
              relative_path=u'projects/{project}/zones/{zone}/linuxAccountViews',
              request_field='',
              request_type_name=u'ComputeaccountsLinuxGetLinuxAccountViewsRequest',
              response_type_name=u'LinuxGetLinuxAccountViewsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def GetAuthorizedKeysView(self, request, global_params=None):
      """Returns a list of authorized public keys for a specific user account.

      Args:
        request: (ComputeaccountsLinuxGetAuthorizedKeysViewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LinuxGetAuthorizedKeysViewResponse) The response message.
      """
      config = self.GetMethodConfig('GetAuthorizedKeysView')
      return self._RunMethod(
          config, request, global_params=global_params)

    def GetLinuxAccountViews(self, request, global_params=None):
      """Retrieves a list of user accounts for an instance within a specific project.

      Args:
        request: (ComputeaccountsLinuxGetLinuxAccountViewsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LinuxGetLinuxAccountViewsResponse) The response message.
      """
      config = self.GetMethodConfig('GetLinuxAccountViews')
      return self._RunMethod(
          config, request, global_params=global_params)

  class UsersService(base_api.BaseApiService):
    """Service class for the users resource."""

    _NAME = u'users'

    def __init__(self, client):
      super(ComputeaccountsStagingAlpha.UsersService, self).__init__(client)
      self._method_configs = {
          'AddPublicKey': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.users.addPublicKey',
              ordered_params=[u'project', u'user'],
              path_params=[u'project', u'user'],
              query_params=[],
              relative_path=u'projects/{project}/global/users/{user}/addPublicKey',
              request_field=u'publicKey',
              request_type_name=u'ComputeaccountsUsersAddPublicKeyRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'computeaccounts.users.delete',
              ordered_params=[u'project', u'user'],
              path_params=[u'project', u'user'],
              query_params=[],
              relative_path=u'projects/{project}/global/users/{user}',
              request_field='',
              request_type_name=u'ComputeaccountsUsersDeleteRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'computeaccounts.users.get',
              ordered_params=[u'project', u'user'],
              path_params=[u'project', u'user'],
              query_params=[],
              relative_path=u'projects/{project}/global/users/{user}',
              request_field='',
              request_type_name=u'ComputeaccountsUsersGetRequest',
              response_type_name=u'User',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.users.insert',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[],
              relative_path=u'projects/{project}/global/users',
              request_field=u'user',
              request_type_name=u'ComputeaccountsUsersInsertRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'computeaccounts.users.list',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[u'filter', u'maxResults', u'pageToken'],
              relative_path=u'projects/{project}/global/users',
              request_field='',
              request_type_name=u'ComputeaccountsUsersListRequest',
              response_type_name=u'UserList',
              supports_download=False,
          ),
          'RemovePublicKey': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'computeaccounts.users.removePublicKey',
              ordered_params=[u'project', u'user', u'fingerprint'],
              path_params=[u'project', u'user'],
              query_params=[u'fingerprint'],
              relative_path=u'projects/{project}/global/users/{user}/removePublicKey',
              request_field='',
              request_type_name=u'ComputeaccountsUsersRemovePublicKeyRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def AddPublicKey(self, request, global_params=None):
      """Adds a public key to the specified User resource with the data included in the request.

      Args:
        request: (ComputeaccountsUsersAddPublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddPublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the specified User resource.

      Args:
        request: (ComputeaccountsUsersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the specified User resource.

      Args:
        request: (ComputeaccountsUsersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (User) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a User resource in the specified project using the data included in the request.

      Args:
        request: (ComputeaccountsUsersInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves a list of users contained within the specified project.

      Args:
        request: (ComputeaccountsUsersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def RemovePublicKey(self, request, global_params=None):
      """Removes the specified public key from the user.

      Args:
        request: (ComputeaccountsUsersRemovePublicKeyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('RemovePublicKey')
      return self._RunMethod(
          config, request, global_params=global_params)
