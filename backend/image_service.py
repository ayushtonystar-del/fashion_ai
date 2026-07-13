from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
)

pipe.to("cuda")

def generate_image(prompt):

    image = pipe(
        prompt,
        num_inference_steps=30
    ).images[0]

    image.save(
        "outputs/generated/result.png"
    )

    return "outputs/generated/result.png"