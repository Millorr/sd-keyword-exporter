import modules.scripts as scripts
import gradio as gr
import json

from modules import script_callbacks, errors
"""
enabled = True

def onChangeCheckbox(value):
    global enabled
    enabled = value

class ParameterExportScript(scripts.Script):
    def show(self, _):
        return scripts.AlwaysVisible

    def ui(self, _):
        enabled = gr.Checkbox(True, label="Enable auto parameter export")
        enabled.change(onChangeCheckbox, inputs=enabled)
"""
def on_image_saved(imageSaveParams: script_callbacks.ImageSaveParams):
    #global enabled
    #if not enabled or "grid" in imageSaveParams.filename:
    #    return
    try:
        params = imageSaveParams.p
        if params is None:
            return
        result = {}
        result["prompt"] = params.prompt
        result["negative_prompt"] = params.negative_prompt
        result["seed"] = params.seed
        result["variation_seed"] = params.subseed
        result["variation_strength"] = params.subseed_strength
        result["sampler_name"] = params.sampler_name
        result["steps"] = params.steps
        result["cfg_scale"] = params.cfg_scale
        result["width"] = params.width
        result["height"] = params.height
        result["restore_faces"] = params.restore_faces
        result["tiling"] = params.tiling
        result["hires"] = params.enable_hr
        result["hires_upscaler"] = params.hr_upscaler
        result["hires_upscale"] = params.hr_scale
        result["hires_steps"] = params.hr_second_pass_steps
        result["hires_denoising_strength"] = params.denoising_strength or 0

        filename = imageSaveParams.filename.replace(".png", ".json").replace(".jpg", ".json")
        print("Saving parameters to " + filename)
        with open(filename, "w") as f:
            json.dump(result, f, indent=4)

    except Exception as e:
        errors.display_once(e, "parameter-export")


script_callbacks.on_image_saved(on_image_saved)
