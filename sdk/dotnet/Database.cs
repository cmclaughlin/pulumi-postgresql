// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.PostgreSql
{
    /// <summary>
    /// The ``postgresql..Database`` resource creates and manages [database
    /// objects](https://www.postgresql.org/docs/current/static/managing-databases.html)
    /// within a PostgreSQL server instance.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/database.html.markdown.
    /// </summary>
    public partial class Database : Pulumi.CustomResource
    {
        /// <summary>
        /// If `false` then no one can connect to this
        /// database. The default is `true`, allowing connections (except as restricted by
        /// other mechanisms, such as `GRANT` or `REVOKE CONNECT`).
        /// </summary>
        [Output("allowConnections")]
        public Output<bool?> AllowConnections { get; private set; } = null!;

        /// <summary>
        /// How many concurrent connections can be
        /// established to this database. `-1` (the default) means no limit.
        /// </summary>
        [Output("connectionLimit")]
        public Output<int?> ConnectionLimit { get; private set; } = null!;

        /// <summary>
        /// Character set encoding to use in the new database
        /// </summary>
        [Output("encoding")]
        public Output<string> Encoding { get; private set; } = null!;

        /// <summary>
        /// If `true`, then this database can be cloned by any
        /// user with `CREATEDB` privileges; if `false` (the default), then only
        /// superusers or the owner of the database can clone it.
        /// </summary>
        [Output("isTemplate")]
        public Output<bool> IsTemplate { get; private set; } = null!;

        /// <summary>
        /// Collation order (LC_COLLATE) to use in the new database
        /// </summary>
        [Output("lcCollate")]
        public Output<string> LcCollate { get; private set; } = null!;

        /// <summary>
        /// Character classification (LC_CTYPE) to use in the new database
        /// </summary>
        [Output("lcCtype")]
        public Output<string> LcCtype { get; private set; } = null!;

        /// <summary>
        /// The name of the database. Must be unique on the PostgreSQL
        /// server instance where it is configured.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The role name of the user who will own the database, or
        /// `DEFAULT` to use the default (namely, the user executing the command). To
        /// create a database owned by another role or to change the owner of an existing
        /// database, you must be a direct or indirect member of the specified role, or
        /// the username in the provider is a superuser.
        /// </summary>
        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        /// <summary>
        /// The name of the tablespace that will be
        /// associated with the database, or `DEFAULT` to use the template database's
        /// tablespace.  This tablespace will be the default tablespace used for objects
        /// created in this database.
        /// </summary>
        [Output("tablespaceName")]
        public Output<string> TablespaceName { get; private set; } = null!;

        /// <summary>
        /// The name of the template from which to create the new database
        /// </summary>
        [Output("template")]
        public Output<string> Template { get; private set; } = null!;


        /// <summary>
        /// Create a Database resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Database(string name, DatabaseArgs? args = null, CustomResourceOptions? options = null)
            : base("postgresql:index/database:Database", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Database(string name, Input<string> id, DatabaseState? state = null, CustomResourceOptions? options = null)
            : base("postgresql:index/database:Database", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Database resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Database Get(string name, Input<string> id, DatabaseState? state = null, CustomResourceOptions? options = null)
        {
            return new Database(name, id, state, options);
        }
    }

    public sealed class DatabaseArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If `false` then no one can connect to this
        /// database. The default is `true`, allowing connections (except as restricted by
        /// other mechanisms, such as `GRANT` or `REVOKE CONNECT`).
        /// </summary>
        [Input("allowConnections")]
        public Input<bool>? AllowConnections { get; set; }

        /// <summary>
        /// How many concurrent connections can be
        /// established to this database. `-1` (the default) means no limit.
        /// </summary>
        [Input("connectionLimit")]
        public Input<int>? ConnectionLimit { get; set; }

        /// <summary>
        /// Character set encoding to use in the new database
        /// </summary>
        [Input("encoding")]
        public Input<string>? Encoding { get; set; }

        /// <summary>
        /// If `true`, then this database can be cloned by any
        /// user with `CREATEDB` privileges; if `false` (the default), then only
        /// superusers or the owner of the database can clone it.
        /// </summary>
        [Input("isTemplate")]
        public Input<bool>? IsTemplate { get; set; }

        /// <summary>
        /// Collation order (LC_COLLATE) to use in the new database
        /// </summary>
        [Input("lcCollate")]
        public Input<string>? LcCollate { get; set; }

        /// <summary>
        /// Character classification (LC_CTYPE) to use in the new database
        /// </summary>
        [Input("lcCtype")]
        public Input<string>? LcCtype { get; set; }

        /// <summary>
        /// The name of the database. Must be unique on the PostgreSQL
        /// server instance where it is configured.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The role name of the user who will own the database, or
        /// `DEFAULT` to use the default (namely, the user executing the command). To
        /// create a database owned by another role or to change the owner of an existing
        /// database, you must be a direct or indirect member of the specified role, or
        /// the username in the provider is a superuser.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        /// <summary>
        /// The name of the tablespace that will be
        /// associated with the database, or `DEFAULT` to use the template database's
        /// tablespace.  This tablespace will be the default tablespace used for objects
        /// created in this database.
        /// </summary>
        [Input("tablespaceName")]
        public Input<string>? TablespaceName { get; set; }

        /// <summary>
        /// The name of the template from which to create the new database
        /// </summary>
        [Input("template")]
        public Input<string>? Template { get; set; }

        public DatabaseArgs()
        {
        }
    }

    public sealed class DatabaseState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If `false` then no one can connect to this
        /// database. The default is `true`, allowing connections (except as restricted by
        /// other mechanisms, such as `GRANT` or `REVOKE CONNECT`).
        /// </summary>
        [Input("allowConnections")]
        public Input<bool>? AllowConnections { get; set; }

        /// <summary>
        /// How many concurrent connections can be
        /// established to this database. `-1` (the default) means no limit.
        /// </summary>
        [Input("connectionLimit")]
        public Input<int>? ConnectionLimit { get; set; }

        /// <summary>
        /// Character set encoding to use in the new database
        /// </summary>
        [Input("encoding")]
        public Input<string>? Encoding { get; set; }

        /// <summary>
        /// If `true`, then this database can be cloned by any
        /// user with `CREATEDB` privileges; if `false` (the default), then only
        /// superusers or the owner of the database can clone it.
        /// </summary>
        [Input("isTemplate")]
        public Input<bool>? IsTemplate { get; set; }

        /// <summary>
        /// Collation order (LC_COLLATE) to use in the new database
        /// </summary>
        [Input("lcCollate")]
        public Input<string>? LcCollate { get; set; }

        /// <summary>
        /// Character classification (LC_CTYPE) to use in the new database
        /// </summary>
        [Input("lcCtype")]
        public Input<string>? LcCtype { get; set; }

        /// <summary>
        /// The name of the database. Must be unique on the PostgreSQL
        /// server instance where it is configured.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The role name of the user who will own the database, or
        /// `DEFAULT` to use the default (namely, the user executing the command). To
        /// create a database owned by another role or to change the owner of an existing
        /// database, you must be a direct or indirect member of the specified role, or
        /// the username in the provider is a superuser.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        /// <summary>
        /// The name of the tablespace that will be
        /// associated with the database, or `DEFAULT` to use the template database's
        /// tablespace.  This tablespace will be the default tablespace used for objects
        /// created in this database.
        /// </summary>
        [Input("tablespaceName")]
        public Input<string>? TablespaceName { get; set; }

        /// <summary>
        /// The name of the template from which to create the new database
        /// </summary>
        [Input("template")]
        public Input<string>? Template { get; set; }

        public DatabaseState()
        {
        }
    }
}
