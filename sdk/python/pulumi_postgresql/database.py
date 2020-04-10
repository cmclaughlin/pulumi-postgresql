# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Database(pulumi.CustomResource):
    allow_connections: pulumi.Output[bool]
    """
    If `false` then no one can connect to this
    database. The default is `true`, allowing connections (except as restricted by
    other mechanisms, such as `GRANT` or `REVOKE CONNECT`).
    """
    connection_limit: pulumi.Output[float]
    """
    How many concurrent connections can be
    established to this database. `-1` (the default) means no limit.
    """
    encoding: pulumi.Output[str]
    """
    Character set encoding to use in the new database
    """
    is_template: pulumi.Output[bool]
    """
    If `true`, then this database can be cloned by any
    user with `CREATEDB` privileges; if `false` (the default), then only
    superusers or the owner of the database can clone it.
    """
    lc_collate: pulumi.Output[str]
    """
    Collation order (LC_COLLATE) to use in the new database
    """
    lc_ctype: pulumi.Output[str]
    """
    Character classification (LC_CTYPE) to use in the new database
    """
    name: pulumi.Output[str]
    """
    The name of the database. Must be unique on the PostgreSQL
    server instance where it is configured.
    """
    owner: pulumi.Output[str]
    """
    The role name of the user who will own the database, or
    `DEFAULT` to use the default (namely, the user executing the command). To
    create a database owned by another role or to change the owner of an existing
    database, you must be a direct or indirect member of the specified role, or
    the username in the provider is a superuser.
    """
    tablespace_name: pulumi.Output[str]
    """
    The name of the tablespace that will be
    associated with the database, or `DEFAULT` to use the template database's
    tablespace.  This tablespace will be the default tablespace used for objects
    created in this database.
    """
    template: pulumi.Output[str]
    """
    The name of the template from which to create the new database
    """
    def __init__(__self__, resource_name, opts=None, allow_connections=None, connection_limit=None, encoding=None, is_template=None, lc_collate=None, lc_ctype=None, name=None, owner=None, tablespace_name=None, template=None, __props__=None, __name__=None, __opts__=None):
        """
        The ``.Database`` resource creates and manages [database
        objects](https://www.postgresql.org/docs/current/static/managing-databases.html)
        within a PostgreSQL server instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_connections: If `false` then no one can connect to this
               database. The default is `true`, allowing connections (except as restricted by
               other mechanisms, such as `GRANT` or `REVOKE CONNECT`).
        :param pulumi.Input[float] connection_limit: How many concurrent connections can be
               established to this database. `-1` (the default) means no limit.
        :param pulumi.Input[str] encoding: Character set encoding to use in the new database
        :param pulumi.Input[bool] is_template: If `true`, then this database can be cloned by any
               user with `CREATEDB` privileges; if `false` (the default), then only
               superusers or the owner of the database can clone it.
        :param pulumi.Input[str] lc_collate: Collation order (LC_COLLATE) to use in the new database
        :param pulumi.Input[str] lc_ctype: Character classification (LC_CTYPE) to use in the new database
        :param pulumi.Input[str] name: The name of the database. Must be unique on the PostgreSQL
               server instance where it is configured.
        :param pulumi.Input[str] owner: The role name of the user who will own the database, or
               `DEFAULT` to use the default (namely, the user executing the command). To
               create a database owned by another role or to change the owner of an existing
               database, you must be a direct or indirect member of the specified role, or
               the username in the provider is a superuser.
        :param pulumi.Input[str] tablespace_name: The name of the tablespace that will be
               associated with the database, or `DEFAULT` to use the template database's
               tablespace.  This tablespace will be the default tablespace used for objects
               created in this database.
        :param pulumi.Input[str] template: The name of the template from which to create the new database
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

            __props__['allow_connections'] = allow_connections
            __props__['connection_limit'] = connection_limit
            __props__['encoding'] = encoding
            __props__['is_template'] = is_template
            __props__['lc_collate'] = lc_collate
            __props__['lc_ctype'] = lc_ctype
            __props__['name'] = name
            __props__['owner'] = owner
            __props__['tablespace_name'] = tablespace_name
            __props__['template'] = template
        super(Database, __self__).__init__(
            'postgresql:index/database:Database',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, allow_connections=None, connection_limit=None, encoding=None, is_template=None, lc_collate=None, lc_ctype=None, name=None, owner=None, tablespace_name=None, template=None):
        """
        Get an existing Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_connections: If `false` then no one can connect to this
               database. The default is `true`, allowing connections (except as restricted by
               other mechanisms, such as `GRANT` or `REVOKE CONNECT`).
        :param pulumi.Input[float] connection_limit: How many concurrent connections can be
               established to this database. `-1` (the default) means no limit.
        :param pulumi.Input[str] encoding: Character set encoding to use in the new database
        :param pulumi.Input[bool] is_template: If `true`, then this database can be cloned by any
               user with `CREATEDB` privileges; if `false` (the default), then only
               superusers or the owner of the database can clone it.
        :param pulumi.Input[str] lc_collate: Collation order (LC_COLLATE) to use in the new database
        :param pulumi.Input[str] lc_ctype: Character classification (LC_CTYPE) to use in the new database
        :param pulumi.Input[str] name: The name of the database. Must be unique on the PostgreSQL
               server instance where it is configured.
        :param pulumi.Input[str] owner: The role name of the user who will own the database, or
               `DEFAULT` to use the default (namely, the user executing the command). To
               create a database owned by another role or to change the owner of an existing
               database, you must be a direct or indirect member of the specified role, or
               the username in the provider is a superuser.
        :param pulumi.Input[str] tablespace_name: The name of the tablespace that will be
               associated with the database, or `DEFAULT` to use the template database's
               tablespace.  This tablespace will be the default tablespace used for objects
               created in this database.
        :param pulumi.Input[str] template: The name of the template from which to create the new database
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allow_connections"] = allow_connections
        __props__["connection_limit"] = connection_limit
        __props__["encoding"] = encoding
        __props__["is_template"] = is_template
        __props__["lc_collate"] = lc_collate
        __props__["lc_ctype"] = lc_ctype
        __props__["name"] = name
        __props__["owner"] = owner
        __props__["tablespace_name"] = tablespace_name
        __props__["template"] = template
        return Database(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

