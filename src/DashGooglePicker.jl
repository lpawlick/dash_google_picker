
module DashGooglePicker
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/googlepicker.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_google_picker",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-GooglePicker.js",
    external_url = "https://unpkg.com/dash_google_picker@0.0.1/dash_google_picker/async-GooglePicker.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-GooglePicker.js.map",
    external_url = "https://unpkg.com/dash_google_picker@0.0.1/dash_google_picker/async-GooglePicker.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_google_picker.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_google_picker.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
