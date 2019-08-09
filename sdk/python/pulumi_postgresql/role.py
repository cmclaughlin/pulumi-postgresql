# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Role(pulumi.CustomResource):
    bypass_row_level_security: pulumi.Output[bool]
    """
    Defines whether a role bypasses every
    row-level security (RLS) policy.  Default value is `false`.
    """
    connection_limit: pulumi.Output[float]
    """
    If this role can log in, this specifies how
    many concurrent connections the role can establish. `-1` (the default) means no
    limit.
    """
    create_database: pulumi.Output[bool]
    """
    Defines a role's ability to execute `CREATE
    DATABASE`.  Default value is `false`.
    """
    create_role: pulumi.Output[bool]
    """
    Defines a role's ability to execute `CREATE ROLE`.
    A role with this privilege can also alter and drop other roles.  Default value
    is `false`.
    """
    encrypted: pulumi.Output[str]
    encrypted_password: pulumi.Output[bool]
    """
    Defines whether the password is stored
    encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
    is always set (to the conservative and safe value), but may interfere with the
    behavior of
    [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).
    """
    inherit: pulumi.Output[bool]
    """
    Defines whether a role "inherits" the privileges of
    roles it is a member of.  Default value is `true`.
    """
    login: pulumi.Output[bool]
    """
    Defines whether role is allowed to log in.  Roles without
    this attribute are useful for managing database privileges, but are not users
    in the usual sense of the word.  Default value is `false`.
    """
    name: pulumi.Output[str]
    """
    The name of the role. Must be unique on the PostgreSQL
    server instance where it is configured.
    """
    password: pulumi.Output[str]
    """
    Sets the role's password. A password is only of use
    for roles having the `login` attribute set to true.
    """
    replication: pulumi.Output[bool]
    """
    Defines whether a role is allowed to initiate
    streaming replication or put the system in and out of backup mode.  Default
    value is `false`
    """
    roles: pulumi.Output[list]
    """
    Defines list of roles which will be granted to this new role.
    """
    skip_drop_role: pulumi.Output[bool]
    """
    When a PostgreSQL ROLE exists in multiple
    databases and the ROLE is dropped, the
    [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
    in each of the respective databases must occur before the ROLE can be dropped
    from the catalog.  Set this option to true when there are multiple databases
    in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
    This is the third and final step taken when removing a ROLE from a database.
    """
    skip_reassign_owned: pulumi.Output[bool]
    """
    When a PostgreSQL ROLE exists in multiple
    databases and the ROLE is dropped, a
    [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
    must be executed on each of the respective databases before the `DROP ROLE`
    can be executed to dropped the ROLE from the catalog.  This is the first and
    second steps taken when removing a ROLE from a database (the second step being
    an implicit
    [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).
    """
    superuser: pulumi.Output[bool]
    """
    Defines whether the role is a "superuser", and
    therefore can override all access restrictions within the database.  Default
    value is `false`.
    """
    valid_until: pulumi.Output[str]
    """
    Defines the date and time after which the role's
    password is no longer valid.  Established connections past this `valid_time`
    will have to be manually terminated.  This value corresponds to a PostgreSQL
    datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
    set to `infinity`.  Default is `NULL`, therefore `infinity`.
    """
    def __init__(__self__, resource_name, opts=None, bypass_row_level_security=None, connection_limit=None, create_database=None, create_role=None, encrypted=None, encrypted_password=None, inherit=None, login=None, name=None, password=None, replication=None, roles=None, skip_drop_role=None, skip_reassign_owned=None, superuser=None, valid_until=None, __props__=None, __name__=None, __opts__=None):
        """
        The ``.Role`` resource creates and manages a role on a PostgreSQL
        server.
        
        When a ``.Role`` resource is removed, the PostgreSQL ROLE will
        automatically run a [`REASSIGN
        OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html)
        and [`DROP
        OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html) to
        the `CURRENT_USER` (normally the connected user for the provider).  If the
        specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
        same PostgreSQL Cluster, one PostgreSQL provider per database must be created
        and all but the final ``.Role`` must specify a `skip_drop_role`.
        
        > **Note:** All arguments including role name and password will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bypass_row_level_security: Defines whether a role bypasses every
               row-level security (RLS) policy.  Default value is `false`.
        :param pulumi.Input[float] connection_limit: If this role can log in, this specifies how
               many concurrent connections the role can establish. `-1` (the default) means no
               limit.
        :param pulumi.Input[bool] create_database: Defines a role's ability to execute `CREATE
               DATABASE`.  Default value is `false`.
        :param pulumi.Input[bool] create_role: Defines a role's ability to execute `CREATE ROLE`.
               A role with this privilege can also alter and drop other roles.  Default value
               is `false`.
        :param pulumi.Input[bool] encrypted_password: Defines whether the password is stored
               encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
               is always set (to the conservative and safe value), but may interfere with the
               behavior of
               [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).
        :param pulumi.Input[bool] inherit: Defines whether a role "inherits" the privileges of
               roles it is a member of.  Default value is `true`.
        :param pulumi.Input[bool] login: Defines whether role is allowed to log in.  Roles without
               this attribute are useful for managing database privileges, but are not users
               in the usual sense of the word.  Default value is `false`.
        :param pulumi.Input[str] name: The name of the role. Must be unique on the PostgreSQL
               server instance where it is configured.
        :param pulumi.Input[str] password: Sets the role's password. A password is only of use
               for roles having the `login` attribute set to true.
        :param pulumi.Input[bool] replication: Defines whether a role is allowed to initiate
               streaming replication or put the system in and out of backup mode.  Default
               value is `false`
        :param pulumi.Input[list] roles: Defines list of roles which will be granted to this new role.
        :param pulumi.Input[bool] skip_drop_role: When a PostgreSQL ROLE exists in multiple
               databases and the ROLE is dropped, the
               [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
               in each of the respective databases must occur before the ROLE can be dropped
               from the catalog.  Set this option to true when there are multiple databases
               in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
               This is the third and final step taken when removing a ROLE from a database.
        :param pulumi.Input[bool] skip_reassign_owned: When a PostgreSQL ROLE exists in multiple
               databases and the ROLE is dropped, a
               [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
               must be executed on each of the respective databases before the `DROP ROLE`
               can be executed to dropped the ROLE from the catalog.  This is the first and
               second steps taken when removing a ROLE from a database (the second step being
               an implicit
               [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).
        :param pulumi.Input[bool] superuser: Defines whether the role is a "superuser", and
               therefore can override all access restrictions within the database.  Default
               value is `false`.
        :param pulumi.Input[str] valid_until: Defines the date and time after which the role's
               password is no longer valid.  Established connections past this `valid_time`
               will have to be manually terminated.  This value corresponds to a PostgreSQL
               datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
               set to `infinity`.  Default is `NULL`, therefore `infinity`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/role.html.markdown.
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

            __props__['bypass_row_level_security'] = bypass_row_level_security
            __props__['connection_limit'] = connection_limit
            __props__['create_database'] = create_database
            __props__['create_role'] = create_role
            __props__['encrypted'] = encrypted
            __props__['encrypted_password'] = encrypted_password
            __props__['inherit'] = inherit
            __props__['login'] = login
            __props__['name'] = name
            __props__['password'] = password
            __props__['replication'] = replication
            __props__['roles'] = roles
            __props__['skip_drop_role'] = skip_drop_role
            __props__['skip_reassign_owned'] = skip_reassign_owned
            __props__['superuser'] = superuser
            __props__['valid_until'] = valid_until
        super(Role, __self__).__init__(
            'postgresql:index/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, bypass_row_level_security=None, connection_limit=None, create_database=None, create_role=None, encrypted=None, encrypted_password=None, inherit=None, login=None, name=None, password=None, replication=None, roles=None, skip_drop_role=None, skip_reassign_owned=None, superuser=None, valid_until=None):
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] bypass_row_level_security: Defines whether a role bypasses every
               row-level security (RLS) policy.  Default value is `false`.
        :param pulumi.Input[float] connection_limit: If this role can log in, this specifies how
               many concurrent connections the role can establish. `-1` (the default) means no
               limit.
        :param pulumi.Input[bool] create_database: Defines a role's ability to execute `CREATE
               DATABASE`.  Default value is `false`.
        :param pulumi.Input[bool] create_role: Defines a role's ability to execute `CREATE ROLE`.
               A role with this privilege can also alter and drop other roles.  Default value
               is `false`.
        :param pulumi.Input[bool] encrypted_password: Defines whether the password is stored
               encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
               is always set (to the conservative and safe value), but may interfere with the
               behavior of
               [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).
        :param pulumi.Input[bool] inherit: Defines whether a role "inherits" the privileges of
               roles it is a member of.  Default value is `true`.
        :param pulumi.Input[bool] login: Defines whether role is allowed to log in.  Roles without
               this attribute are useful for managing database privileges, but are not users
               in the usual sense of the word.  Default value is `false`.
        :param pulumi.Input[str] name: The name of the role. Must be unique on the PostgreSQL
               server instance where it is configured.
        :param pulumi.Input[str] password: Sets the role's password. A password is only of use
               for roles having the `login` attribute set to true.
        :param pulumi.Input[bool] replication: Defines whether a role is allowed to initiate
               streaming replication or put the system in and out of backup mode.  Default
               value is `false`
        :param pulumi.Input[list] roles: Defines list of roles which will be granted to this new role.
        :param pulumi.Input[bool] skip_drop_role: When a PostgreSQL ROLE exists in multiple
               databases and the ROLE is dropped, the
               [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
               in each of the respective databases must occur before the ROLE can be dropped
               from the catalog.  Set this option to true when there are multiple databases
               in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
               This is the third and final step taken when removing a ROLE from a database.
        :param pulumi.Input[bool] skip_reassign_owned: When a PostgreSQL ROLE exists in multiple
               databases and the ROLE is dropped, a
               [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
               must be executed on each of the respective databases before the `DROP ROLE`
               can be executed to dropped the ROLE from the catalog.  This is the first and
               second steps taken when removing a ROLE from a database (the second step being
               an implicit
               [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).
        :param pulumi.Input[bool] superuser: Defines whether the role is a "superuser", and
               therefore can override all access restrictions within the database.  Default
               value is `false`.
        :param pulumi.Input[str] valid_until: Defines the date and time after which the role's
               password is no longer valid.  Established connections past this `valid_time`
               will have to be manually terminated.  This value corresponds to a PostgreSQL
               datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
               set to `infinity`.  Default is `NULL`, therefore `infinity`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/role.html.markdown.
        """
        opts = pulumi.ResourceOptions(id=id) if opts is None else opts.merge(pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["bypass_row_level_security"] = bypass_row_level_security
        __props__["connection_limit"] = connection_limit
        __props__["create_database"] = create_database
        __props__["create_role"] = create_role
        __props__["encrypted"] = encrypted
        __props__["encrypted_password"] = encrypted_password
        __props__["inherit"] = inherit
        __props__["login"] = login
        __props__["name"] = name
        __props__["password"] = password
        __props__["replication"] = replication
        __props__["roles"] = roles
        __props__["skip_drop_role"] = skip_drop_role
        __props__["skip_reassign_owned"] = skip_reassign_owned
        __props__["superuser"] = superuser
        __props__["valid_until"] = valid_until
        return Role(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

