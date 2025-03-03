# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "image update",
)
class Update(AAZCommand):
    """Update custom VM images.

    :example: Add or update tags.
        az image update -n ImageName -g ResourceGroup --tags tag1=val1 tag2=val2

    :example: Remove all tags.
        az image update -n ImageName -g resourceGroup --tags
    """

    _aaz_info = {
        "version": "2020-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/images/{}", "2020-06-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.image_name = AAZStrArg(
            options=["-n", "--name", "--image-name"],
            help="The name of the image.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"
        return cls._args_schema

    _args_disk_encryption_set_parameters_update = None

    @classmethod
    def _build_args_disk_encryption_set_parameters_update(cls, _schema):
        if cls._args_disk_encryption_set_parameters_update is not None:
            _schema.id = cls._args_disk_encryption_set_parameters_update.id
            return

        cls._args_disk_encryption_set_parameters_update = AAZObjectArg(
            nullable=True,
        )

        disk_encryption_set_parameters_update = cls._args_disk_encryption_set_parameters_update
        disk_encryption_set_parameters_update.id = AAZStrArg(
            options=["id"],
            help="Resource Id",
            nullable=True,
        )

        _schema.id = cls._args_disk_encryption_set_parameters_update.id

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource Id",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.ImagesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.ImagesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ImagesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "imageName", self.ctx.args.image_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2020-06-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_image_read(cls._schema_on_200)

            return cls._schema_on_200

    class ImagesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "imageName", self.ctx.args.image_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2020-06-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_image_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_disk_encryption_set_parameters_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_disk_encryption_set_parameters_read = None

    @classmethod
    def _build_schema_disk_encryption_set_parameters_read(cls, _schema):
        if cls._schema_disk_encryption_set_parameters_read is not None:
            _schema.id = cls._schema_disk_encryption_set_parameters_read.id
            return

        cls._schema_disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read = AAZObjectType()

        disk_encryption_set_parameters_read = _schema_disk_encryption_set_parameters_read
        disk_encryption_set_parameters_read.id = AAZStrType()

        _schema.id = cls._schema_disk_encryption_set_parameters_read.id

    _schema_image_read = None

    @classmethod
    def _build_schema_image_read(cls, _schema):
        if cls._schema_image_read is not None:
            _schema.id = cls._schema_image_read.id
            _schema.location = cls._schema_image_read.location
            _schema.name = cls._schema_image_read.name
            _schema.properties = cls._schema_image_read.properties
            _schema.tags = cls._schema_image_read.tags
            _schema.type = cls._schema_image_read.type
            return

        cls._schema_image_read = _schema_image_read = AAZObjectType()

        image_read = _schema_image_read
        image_read.id = AAZStrType(
            flags={"read_only": True},
        )
        image_read.location = AAZStrType(
            flags={"required": True},
        )
        image_read.name = AAZStrType(
            flags={"read_only": True},
        )
        image_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        image_read.tags = AAZDictType()
        image_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_image_read.properties
        properties.hyper_v_generation = AAZStrType(
            serialized_name="hyperVGeneration",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.source_virtual_machine = AAZObjectType(
            serialized_name="sourceVirtualMachine",
        )
        cls._build_schema_sub_resource_read(properties.source_virtual_machine)
        properties.storage_profile = AAZObjectType(
            serialized_name="storageProfile",
        )

        storage_profile = _schema_image_read.properties.storage_profile
        storage_profile.data_disks = AAZListType(
            serialized_name="dataDisks",
        )
        storage_profile.os_disk = AAZObjectType(
            serialized_name="osDisk",
        )
        storage_profile.zone_resilient = AAZBoolType(
            serialized_name="zoneResilient",
        )

        data_disks = _schema_image_read.properties.storage_profile.data_disks
        data_disks.Element = AAZObjectType()

        _element = _schema_image_read.properties.storage_profile.data_disks.Element
        _element.blob_uri = AAZStrType(
            serialized_name="blobUri",
        )
        _element.caching = AAZStrType()
        _element.disk_encryption_set = AAZObjectType(
            serialized_name="diskEncryptionSet",
        )
        cls._build_schema_disk_encryption_set_parameters_read(_element.disk_encryption_set)
        _element.disk_size_gb = AAZIntType(
            serialized_name="diskSizeGB",
        )
        _element.lun = AAZIntType(
            flags={"required": True},
        )
        _element.managed_disk = AAZObjectType(
            serialized_name="managedDisk",
        )
        cls._build_schema_sub_resource_read(_element.managed_disk)
        _element.snapshot = AAZObjectType()
        cls._build_schema_sub_resource_read(_element.snapshot)
        _element.storage_account_type = AAZStrType(
            serialized_name="storageAccountType",
        )

        os_disk = _schema_image_read.properties.storage_profile.os_disk
        os_disk.blob_uri = AAZStrType(
            serialized_name="blobUri",
        )
        os_disk.caching = AAZStrType()
        os_disk.disk_encryption_set = AAZObjectType(
            serialized_name="diskEncryptionSet",
        )
        cls._build_schema_disk_encryption_set_parameters_read(os_disk.disk_encryption_set)
        os_disk.disk_size_gb = AAZIntType(
            serialized_name="diskSizeGB",
        )
        os_disk.managed_disk = AAZObjectType(
            serialized_name="managedDisk",
        )
        cls._build_schema_sub_resource_read(os_disk.managed_disk)
        os_disk.os_state = AAZStrType(
            serialized_name="osState",
            flags={"required": True},
        )
        os_disk.os_type = AAZStrType(
            serialized_name="osType",
            flags={"required": True},
        )
        os_disk.snapshot = AAZObjectType()
        cls._build_schema_sub_resource_read(os_disk.snapshot)
        os_disk.storage_account_type = AAZStrType(
            serialized_name="storageAccountType",
        )

        tags = _schema_image_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_image_read.id
        _schema.location = cls._schema_image_read.location
        _schema.name = cls._schema_image_read.name
        _schema.properties = cls._schema_image_read.properties
        _schema.tags = cls._schema_image_read.tags
        _schema.type = cls._schema_image_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
