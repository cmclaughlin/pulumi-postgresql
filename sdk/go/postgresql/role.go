// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package postgresql

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ``postgresql_role`` resource creates and manages a role on a PostgreSQL
// server.
// 
// When a ``postgresql_role`` resource is removed, the PostgreSQL ROLE will
// automatically run a [`REASSIGN
// OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html)
// and [`DROP
// OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html) to
// the `CURRENT_USER` (normally the connected user for the provider).  If the
// specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
// same PostgreSQL Cluster, one PostgreSQL provider per database must be created
// and all but the final ``postgresql_role`` must specify a `skip_drop_role`.
// 
// > **Note:** All arguments including role name and password will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/role.html.markdown.
type Role struct {
	s *pulumi.ResourceState
}

// NewRole registers a new resource with the given unique name, arguments, and options.
func NewRole(ctx *pulumi.Context,
	name string, args *RoleArgs, opts ...pulumi.ResourceOpt) (*Role, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bypassRowLevelSecurity"] = nil
		inputs["connectionLimit"] = nil
		inputs["createDatabase"] = nil
		inputs["createRole"] = nil
		inputs["encrypted"] = nil
		inputs["encryptedPassword"] = nil
		inputs["inherit"] = nil
		inputs["login"] = nil
		inputs["name"] = nil
		inputs["password"] = nil
		inputs["replication"] = nil
		inputs["roles"] = nil
		inputs["skipDropRole"] = nil
		inputs["skipReassignOwned"] = nil
		inputs["superuser"] = nil
		inputs["validUntil"] = nil
	} else {
		inputs["bypassRowLevelSecurity"] = args.BypassRowLevelSecurity
		inputs["connectionLimit"] = args.ConnectionLimit
		inputs["createDatabase"] = args.CreateDatabase
		inputs["createRole"] = args.CreateRole
		inputs["encrypted"] = args.Encrypted
		inputs["encryptedPassword"] = args.EncryptedPassword
		inputs["inherit"] = args.Inherit
		inputs["login"] = args.Login
		inputs["name"] = args.Name
		inputs["password"] = args.Password
		inputs["replication"] = args.Replication
		inputs["roles"] = args.Roles
		inputs["skipDropRole"] = args.SkipDropRole
		inputs["skipReassignOwned"] = args.SkipReassignOwned
		inputs["superuser"] = args.Superuser
		inputs["validUntil"] = args.ValidUntil
	}
	s, err := ctx.RegisterResource("postgresql:index/role:Role", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Role{s: s}, nil
}

// GetRole gets an existing Role resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRole(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RoleState, opts ...pulumi.ResourceOpt) (*Role, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bypassRowLevelSecurity"] = state.BypassRowLevelSecurity
		inputs["connectionLimit"] = state.ConnectionLimit
		inputs["createDatabase"] = state.CreateDatabase
		inputs["createRole"] = state.CreateRole
		inputs["encrypted"] = state.Encrypted
		inputs["encryptedPassword"] = state.EncryptedPassword
		inputs["inherit"] = state.Inherit
		inputs["login"] = state.Login
		inputs["name"] = state.Name
		inputs["password"] = state.Password
		inputs["replication"] = state.Replication
		inputs["roles"] = state.Roles
		inputs["skipDropRole"] = state.SkipDropRole
		inputs["skipReassignOwned"] = state.SkipReassignOwned
		inputs["superuser"] = state.Superuser
		inputs["validUntil"] = state.ValidUntil
	}
	s, err := ctx.ReadResource("postgresql:index/role:Role", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Role{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Role) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Role) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Defines whether a role bypasses every
// row-level security (RLS) policy.  Default value is `false`.
func (r *Role) BypassRowLevelSecurity() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["bypassRowLevelSecurity"])
}

// If this role can log in, this specifies how
// many concurrent connections the role can establish. `-1` (the default) means no
// limit.
func (r *Role) ConnectionLimit() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["connectionLimit"])
}

// Defines a role's ability to execute `CREATE
// DATABASE`.  Default value is `false`.
func (r *Role) CreateDatabase() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["createDatabase"])
}

// Defines a role's ability to execute `CREATE ROLE`.
// A role with this privilege can also alter and drop other roles.  Default value
// is `false`.
func (r *Role) CreateRole() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["createRole"])
}

func (r *Role) Encrypted() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["encrypted"])
}

// Defines whether the password is stored
// encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
// is always set (to the conservative and safe value), but may interfere with the
// behavior of
// [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).
func (r *Role) EncryptedPassword() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["encryptedPassword"])
}

// Defines whether a role "inherits" the privileges of
// roles it is a member of.  Default value is `true`.
func (r *Role) Inherit() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["inherit"])
}

// Defines whether role is allowed to log in.  Roles without
// this attribute are useful for managing database privileges, but are not users
// in the usual sense of the word.  Default value is `false`.
func (r *Role) Login() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["login"])
}

// The name of the role. Must be unique on the PostgreSQL
// server instance where it is configured.
func (r *Role) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Sets the role's password. A password is only of use
// for roles having the `login` attribute set to true.
func (r *Role) Password() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["password"])
}

// Defines whether a role is allowed to initiate
// streaming replication or put the system in and out of backup mode.  Default
// value is `false`
func (r *Role) Replication() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["replication"])
}

// Defines list of roles which will be granted to this new role.
func (r *Role) Roles() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["roles"])
}

// When a PostgreSQL ROLE exists in multiple
// databases and the ROLE is dropped, the
// [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
// in each of the respective databases must occur before the ROLE can be dropped
// from the catalog.  Set this option to true when there are multiple databases
// in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
// This is the third and final step taken when removing a ROLE from a database.
func (r *Role) SkipDropRole() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["skipDropRole"])
}

// When a PostgreSQL ROLE exists in multiple
// databases and the ROLE is dropped, a
// [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
// must be executed on each of the respective databases before the `DROP ROLE`
// can be executed to dropped the ROLE from the catalog.  This is the first and
// second steps taken when removing a ROLE from a database (the second step being
// an implicit
// [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).
func (r *Role) SkipReassignOwned() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["skipReassignOwned"])
}

// Defines whether the role is a "superuser", and
// therefore can override all access restrictions within the database.  Default
// value is `false`.
func (r *Role) Superuser() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["superuser"])
}

// Defines the date and time after which the role's
// password is no longer valid.  Established connections past this `valid_time`
// will have to be manually terminated.  This value corresponds to a PostgreSQL
// datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
// set to `infinity`.  Default is `NULL`, therefore `infinity`.
func (r *Role) ValidUntil() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["validUntil"])
}

// Input properties used for looking up and filtering Role resources.
type RoleState struct {
	// Defines whether a role bypasses every
	// row-level security (RLS) policy.  Default value is `false`.
	BypassRowLevelSecurity interface{}
	// If this role can log in, this specifies how
	// many concurrent connections the role can establish. `-1` (the default) means no
	// limit.
	ConnectionLimit interface{}
	// Defines a role's ability to execute `CREATE
	// DATABASE`.  Default value is `false`.
	CreateDatabase interface{}
	// Defines a role's ability to execute `CREATE ROLE`.
	// A role with this privilege can also alter and drop other roles.  Default value
	// is `false`.
	CreateRole interface{}
	Encrypted interface{}
	// Defines whether the password is stored
	// encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
	// is always set (to the conservative and safe value), but may interfere with the
	// behavior of
	// [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).
	EncryptedPassword interface{}
	// Defines whether a role "inherits" the privileges of
	// roles it is a member of.  Default value is `true`.
	Inherit interface{}
	// Defines whether role is allowed to log in.  Roles without
	// this attribute are useful for managing database privileges, but are not users
	// in the usual sense of the word.  Default value is `false`.
	Login interface{}
	// The name of the role. Must be unique on the PostgreSQL
	// server instance where it is configured.
	Name interface{}
	// Sets the role's password. A password is only of use
	// for roles having the `login` attribute set to true.
	Password interface{}
	// Defines whether a role is allowed to initiate
	// streaming replication or put the system in and out of backup mode.  Default
	// value is `false`
	Replication interface{}
	// Defines list of roles which will be granted to this new role.
	Roles interface{}
	// When a PostgreSQL ROLE exists in multiple
	// databases and the ROLE is dropped, the
	// [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
	// in each of the respective databases must occur before the ROLE can be dropped
	// from the catalog.  Set this option to true when there are multiple databases
	// in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
	// This is the third and final step taken when removing a ROLE from a database.
	SkipDropRole interface{}
	// When a PostgreSQL ROLE exists in multiple
	// databases and the ROLE is dropped, a
	// [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
	// must be executed on each of the respective databases before the `DROP ROLE`
	// can be executed to dropped the ROLE from the catalog.  This is the first and
	// second steps taken when removing a ROLE from a database (the second step being
	// an implicit
	// [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).
	SkipReassignOwned interface{}
	// Defines whether the role is a "superuser", and
	// therefore can override all access restrictions within the database.  Default
	// value is `false`.
	Superuser interface{}
	// Defines the date and time after which the role's
	// password is no longer valid.  Established connections past this `valid_time`
	// will have to be manually terminated.  This value corresponds to a PostgreSQL
	// datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
	// set to `infinity`.  Default is `NULL`, therefore `infinity`.
	ValidUntil interface{}
}

// The set of arguments for constructing a Role resource.
type RoleArgs struct {
	// Defines whether a role bypasses every
	// row-level security (RLS) policy.  Default value is `false`.
	BypassRowLevelSecurity interface{}
	// If this role can log in, this specifies how
	// many concurrent connections the role can establish. `-1` (the default) means no
	// limit.
	ConnectionLimit interface{}
	// Defines a role's ability to execute `CREATE
	// DATABASE`.  Default value is `false`.
	CreateDatabase interface{}
	// Defines a role's ability to execute `CREATE ROLE`.
	// A role with this privilege can also alter and drop other roles.  Default value
	// is `false`.
	CreateRole interface{}
	Encrypted interface{}
	// Defines whether the password is stored
	// encrypted in the system catalogs.  Default value is `true`.  NOTE: this value
	// is always set (to the conservative and safe value), but may interfere with the
	// behavior of
	// [PostgreSQL's `password_encryption` setting](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION).
	EncryptedPassword interface{}
	// Defines whether a role "inherits" the privileges of
	// roles it is a member of.  Default value is `true`.
	Inherit interface{}
	// Defines whether role is allowed to log in.  Roles without
	// this attribute are useful for managing database privileges, but are not users
	// in the usual sense of the word.  Default value is `false`.
	Login interface{}
	// The name of the role. Must be unique on the PostgreSQL
	// server instance where it is configured.
	Name interface{}
	// Sets the role's password. A password is only of use
	// for roles having the `login` attribute set to true.
	Password interface{}
	// Defines whether a role is allowed to initiate
	// streaming replication or put the system in and out of backup mode.  Default
	// value is `false`
	Replication interface{}
	// Defines list of roles which will be granted to this new role.
	Roles interface{}
	// When a PostgreSQL ROLE exists in multiple
	// databases and the ROLE is dropped, the
	// [cleanup of ownership of objects](https://www.postgresql.org/docs/current/static/role-removal.html)
	// in each of the respective databases must occur before the ROLE can be dropped
	// from the catalog.  Set this option to true when there are multiple databases
	// in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
	// This is the third and final step taken when removing a ROLE from a database.
	SkipDropRole interface{}
	// When a PostgreSQL ROLE exists in multiple
	// databases and the ROLE is dropped, a
	// [`REASSIGN OWNED`](https://www.postgresql.org/docs/current/static/sql-reassign-owned.html) in
	// must be executed on each of the respective databases before the `DROP ROLE`
	// can be executed to dropped the ROLE from the catalog.  This is the first and
	// second steps taken when removing a ROLE from a database (the second step being
	// an implicit
	// [`DROP OWNED`](https://www.postgresql.org/docs/current/static/sql-drop-owned.html)).
	SkipReassignOwned interface{}
	// Defines whether the role is a "superuser", and
	// therefore can override all access restrictions within the database.  Default
	// value is `false`.
	Superuser interface{}
	// Defines the date and time after which the role's
	// password is no longer valid.  Established connections past this `valid_time`
	// will have to be manually terminated.  This value corresponds to a PostgreSQL
	// datetime. If omitted or the magic value `NULL` is used, `valid_until` will be
	// set to `infinity`.  Default is `NULL`, therefore `infinity`.
	ValidUntil interface{}
}
