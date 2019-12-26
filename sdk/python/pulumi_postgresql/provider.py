# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, resource_name, opts=None, connect_timeout=None, database=None, database_username=None, expected_version=None, host=None, max_connections=None, password=None, port=None, ssl_mode=None, sslmode=None, superuser=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        The provider type for the postgresql package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/index.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if connect_timeout is None:
                connect_timeout = utilities.get_env_int('PGCONNECT_TIMEOUT')
            __props__['connect_timeout'] = pulumi.Output.from_input(connect_timeout).apply(json.dumps) if connect_timeout is not None else None
            if database is None:
                database = utilities.get_env('PGDATABASE')
            __props__['database'] = database
            __props__['database_username'] = database_username
            __props__['expected_version'] = expected_version
            if host is None:
                host = utilities.get_env('PGHOST')
            __props__['host'] = host
            __props__['max_connections'] = pulumi.Output.from_input(max_connections).apply(json.dumps) if max_connections is not None else None
            if password is None:
                password = utilities.get_env('PGPASSWORD')
            __props__['password'] = password
            if port is None:
                port = (utilities.get_env_int('PGPORT') or 5432)
            __props__['port'] = pulumi.Output.from_input(port).apply(json.dumps) if port is not None else None
            __props__['ssl_mode'] = ssl_mode
            if sslmode is None:
                sslmode = utilities.get_env('PGSSLMODE')
            __props__['sslmode'] = sslmode
            __props__['superuser'] = pulumi.Output.from_input(superuser).apply(json.dumps) if superuser is not None else None
            if username is None:
                username = utilities.get_env('PGUSER')
            __props__['username'] = username
        super(Provider, __self__).__init__(
            'postgresql',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get an existing Provider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/index.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        return Provider(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

