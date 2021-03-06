// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The ``postgresql.Grant`` resource creates and manages privileges given to a user for a database schema.
 *
 * > **Note:** This resource needs Postgresql version 9 or above.
 *
 * ## Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as postgresql from "@pulumi/postgresql";
 *
 * const readonlyTables = new postgresql.Grant("readonly_tables", {
 *     database: "test_db",
 *     objectType: "table",
 *     privileges: ["SELECT"],
 *     role: "test_role",
 *     schema: "public",
 * });
 * ```
 */
export class Grant extends pulumi.CustomResource {
    /**
     * Get an existing Grant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GrantState, opts?: pulumi.CustomResourceOptions): Grant {
        return new Grant(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'postgresql:index/grant:Grant';

    /**
     * Returns true if the given object is an instance of Grant.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Grant {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Grant.__pulumiType;
    }

    /**
     * The database to grant privileges on for this role.
     */
    public readonly database!: pulumi.Output<string>;
    /**
     * The PostgreSQL object type to grant the privileges on (one of: table, sequence).
     */
    public readonly objectType!: pulumi.Output<string>;
    /**
     * The list of privileges to grant.
     */
    public readonly privileges!: pulumi.Output<string[]>;
    /**
     * The name of the role to grant privileges on.
     */
    public readonly role!: pulumi.Output<string>;
    /**
     * The database schema to grant privileges on for this role.
     */
    public readonly schema!: pulumi.Output<string | undefined>;
    /**
     * Permit the grant recipient to grant it to others
     */
    public readonly withGrantOption!: pulumi.Output<boolean | undefined>;

    /**
     * Create a Grant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GrantArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GrantArgs | GrantState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GrantState | undefined;
            inputs["database"] = state ? state.database : undefined;
            inputs["objectType"] = state ? state.objectType : undefined;
            inputs["privileges"] = state ? state.privileges : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["schema"] = state ? state.schema : undefined;
            inputs["withGrantOption"] = state ? state.withGrantOption : undefined;
        } else {
            const args = argsOrState as GrantArgs | undefined;
            if (!args || args.database === undefined) {
                throw new Error("Missing required property 'database'");
            }
            if (!args || args.objectType === undefined) {
                throw new Error("Missing required property 'objectType'");
            }
            if (!args || args.privileges === undefined) {
                throw new Error("Missing required property 'privileges'");
            }
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            inputs["database"] = args ? args.database : undefined;
            inputs["objectType"] = args ? args.objectType : undefined;
            inputs["privileges"] = args ? args.privileges : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["schema"] = args ? args.schema : undefined;
            inputs["withGrantOption"] = args ? args.withGrantOption : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Grant.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Grant resources.
 */
export interface GrantState {
    /**
     * The database to grant privileges on for this role.
     */
    readonly database?: pulumi.Input<string>;
    /**
     * The PostgreSQL object type to grant the privileges on (one of: table, sequence).
     */
    readonly objectType?: pulumi.Input<string>;
    /**
     * The list of privileges to grant.
     */
    readonly privileges?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the role to grant privileges on.
     */
    readonly role?: pulumi.Input<string>;
    /**
     * The database schema to grant privileges on for this role.
     */
    readonly schema?: pulumi.Input<string>;
    /**
     * Permit the grant recipient to grant it to others
     */
    readonly withGrantOption?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a Grant resource.
 */
export interface GrantArgs {
    /**
     * The database to grant privileges on for this role.
     */
    readonly database: pulumi.Input<string>;
    /**
     * The PostgreSQL object type to grant the privileges on (one of: table, sequence).
     */
    readonly objectType: pulumi.Input<string>;
    /**
     * The list of privileges to grant.
     */
    readonly privileges: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the role to grant privileges on.
     */
    readonly role: pulumi.Input<string>;
    /**
     * The database schema to grant privileges on for this role.
     */
    readonly schema?: pulumi.Input<string>;
    /**
     * Permit the grant recipient to grant it to others
     */
    readonly withGrantOption?: pulumi.Input<boolean>;
}
