# Week 1 Assignment

## Task 1: 5 Interesting Concepts Learned from the Lectures

## 1. Human Vision is Hard but Feels Easy

Human vision feels easy because the final result reaches our mind directly. We look at something and instantly think: “chair,” “face,” “phone,” “road,” or “danger.” We do not consciously calculate edges, colors, depth, shadows, or object boundaries. The lecture also explains that when we see a chair, we do not sit and think about it for a long time; the recognition just “pops” into our head. But vision is actually hard because many hidden steps happen before that simple feeling.

First, the eye has to collect light. Light passes through the cornea, lens, and other structures, and then gets focused onto the retina. The retina has photoreceptors called rods and cones. Rods help in low light and mostly support monochrome vision, while cones help with detailed color vision. These cells are not evenly spread: cones are concentrated in the fovea, while rods are more common in peripheral vision.

Then the brain processes the signal. The lecture mentions that the visual cortex has areas like V1, which performs low-level operations such as edge detection, and V2, where properties like shape, size, and color start emerging. So our brain is not just “seeing”; it is analyzing the image layer by layer.

The hardest part is that the brain also creates meaning and depth. From a 2D image on the retina, it estimates 3D information using focus, blur, parallax, two-eye disparity, convergence, occlusion, familiar object size, and shading. That means even when we casually understand that one object is near and another is far, our brain has already done a lot of hidden computation.

## 2. Photoreceptors Need Change

Photoreceptors need change because they do not respond strongly to the same visual signal forever. Photoreceptors are light-sensitive cells present in the retina of the eye, mainly rods and cones. Rods help us see in low light, while cones help us see color and fine details. When the same color or light keeps falling on the same photoreceptors for a long time, those cells slowly adapt to it and become less sensitive. This means that the eye starts treating that constant signal as normal background information.

A simple analogy is the sound of a fan: at first we notice it, but after some time our brain starts ignoring it even though the sound is still present. Similarly, if we keep staring at the same visual pattern, the photoreceptors may stop responding strongly to it. The lecture explained this using the purple-dot illusion. In that illusion, when a person stares at a fixed cross in the center, the same purple dots keep stimulating the same retinal cells. After some time, the photoreceptors adapt to the purple color, so the purple dots may appear to fade. When one purple dot disappears, the visual system may create the impression of a green dot because green is roughly the opposite color of purple.

This shows that human vision is not like a normal camera. A camera would continue recording the same purple dots without changing its response, but human vision keeps adapting, filtering, and interpreting the input. To avoid complete fading of a fixed image, our eyes keep making tiny involuntary movements even when we feel that we are staring at one point. These movements include microsaccades, ocular drift, and microtremors. Microsaccades are very small quick jumps of the eye, ocular drift is a slow movement around the fixation point, and microtremors are tiny vibrations. These movements slightly shift the image on the retina so that different photoreceptors keep getting stimulated. Because of this, the visual signal keeps refreshing, and we are able to maintain clear vision. Overall, this concept shows that our eyes are especially good at detecting change, movement, contrast, and sudden differences rather than simply recording a fixed scene passively.

## 3. Computer Vision vs Human Vision in Color Perception

One interesting difference between computer vision and human vision is how they understand color under different lighting conditions. In human vision, the brain does not simply accept the raw color signal coming from the eyes. It also uses context and lighting information to guess the actual color of an object. For example, a white paper may look slightly yellow under a warm bulb, bluish in shadow, and brighter in sunlight, but our brain still understands that the paper is white. This ability is called color constancy.

Computer vision systems, however, usually receive an image as pixel values such as RGB numbers. If the lighting changes, the same object can produce very different pixel values, so a computer may find it harder to recognize that it is still the same object. This is why illumination is an important challenge in computer vision. Human vision is adaptive and context-aware, while computer vision often needs preprocessing, normalization, or training on varied lighting conditions to handle the same problem.

## 4. Image as a Matrix of Light and Its Storage in Memory

One important concept I learned is that a digital image is not just a picture; for a computer, it is a structured collection of numbers representing light. When a camera captures a scene, light from the 3D world falls on a flat 2D sensor, so the image becomes a 2D projection of the real world. At each point on this sensor, the camera records how much light is received. In a grayscale image, this can be stored as a simple 2D matrix where each pixel has one brightness value. A low value means the pixel is dark, while a high value means the pixel is bright. For example, many images use values from 0 to 255, where 0 represents black and 255 represents maximum brightness.

For a color image, one value per pixel is not enough because color needs red, green, and blue information. Therefore, a color image is stored as a 3D tensor with height, width, and channels. The three channels usually represent red, green, and blue. This means every pixel location stores three values: how much red light, how much green light, and how much blue light are present. Combining these three values gives the final color of that pixel. For example, `(255, 0, 0)` represents red, `(0, 255, 0)` represents green, `(0, 0, 255)` represents blue, `(255, 255, 255)` represents white, and `(0, 0, 0)` represents black.

Another important part is addressing pixels. Since an image is a grid, each pixel has a coordinate. In images, the origin is usually at the top-left corner, unlike normal mathematical graphs. The x-coordinate represents the column, and the y-coordinate represents the row. For a color image, we also need the channel coordinate, so a pixel can be addressed as `(x, y, channel)`. For example, `(10, 20, 0)` means column 10, row 20, channel 0. If channel 0 is red, then this gives the red value at that pixel.

After this, the lecture explained how images are stored in memory. Although we think of a color image as a 3D tensor, computer memory is like one long line of values. So the 3D image has to be flattened into a 1D array. For a 2D image, this can be done using row-major order or column-major order. In row-major order, the first row is stored first, then the second row, and so on. In column-major order, the first column is stored first, then the second column, and so on. Most image-processing systems commonly use row-major order.

For color images, there are two common storage formats: HWC and CHW. HWC means height, width, channels. In this format, the red, green, and blue values of one pixel are stored together, like `RGB | RGB | RGB`. This is called channels interleaved. CHW means channels, height, width. In this format, the entire red channel is stored first, then the entire green channel, and then the entire blue channel. This is called channels separated.

The lecture’s pop quiz used the CHW format. For a `1920 × 1080 × 3` image, the index of a pixel `(x, y, z)` in the 1D array is calculated as:

`index = x + y × W + z × W × H`

For the pixel `(15, 192, 2)`, with `W = 1920` and `H = 1080`, the index becomes:

`15 + 192 × 1920 + 2 × 1920 × 1080 = 4,515,855`

This means the pixel value at coordinate `(15, 192, 2)` is stored at position `4,515,855` in the long 1D array. This concept helped me understand that images are not stored as simple pictures inside a computer. They are stored as organized numerical data, with rules for brightness values, color channels, pixel coordinates, and memory layout.

## 5. Color Spaces, HSV, and Image Interpolation

Another interesting concept from the lectures is that the same image can be represented in different color spaces. RGB represents every pixel using red, green, and blue values. This is useful for storing and displaying images, but it is not always intuitive for editing or processing. For example, if we want to make an image more colorful, directly changing red, green, and blue values can be confusing because it may also change the actual color balance of the image.

HSV is another color space that represents the same visual information in a different way. HSV stands for hue, saturation, and value. Hue represents the basic color type, such as red, green, blue, or yellow. Saturation represents how intense or pure the color is. A highly saturated color looks bright and strong, while a low-saturation color looks dull or grayish. Value represents brightness. Increasing value makes an image lighter, while decreasing value makes it darker.

This makes HSV useful for image processing. If we increase saturation, the colors become more intense. If we increase value, the image becomes brighter. If we shift hue, the actual colors change around the color wheel. This is easier than trying to perform the same operations directly in RGB. Even after converting from RGB to HSV, the image is still a 3D tensor, but the meaning of the channels changes from red, green, and blue to hue, saturation, and value.

The lecture also discussed interpolation, which is important for resizing images. An image stores pixel values only at fixed integer coordinates, but when we resize or transform an image, we often need values at non-integer positions. Interpolation is the process of estimating these missing values using nearby known pixels. Nearest neighbor interpolation simply copies the value of the closest pixel, so it is fast but can make the image look blocky. Bilinear interpolation uses the nearest four pixels and takes a weighted average, so the result is usually smoother. This helped me understand that resizing an image is not just stretching it visually; it involves estimating new pixel values in a careful way.


---

## Task 2: Types of Healthcare Reports and Medical Imaging Reports

Healthcare reports are documents used to record and communicate important information about a patient’s health. These reports help doctors, nurses, specialists, hospitals, and patients understand the patient’s condition, tests, diagnosis, treatment, and follow-up plan. Different types of healthcare reports are made for different medical purposes.

Some common types of healthcare reports include **medical history reports**, **laboratory reports**, **pathology reports**, **clinical or progress notes**, **discharge summaries**, **operative reports**, **prescription reports**, and **medical imaging reports**. A medical history report contains information about the patient’s previous illnesses, surgeries, allergies, family history, lifestyle, and past medicines. Laboratory reports contain results of tests done on blood, urine, or other body samples, such as blood sugar, CBC, thyroid profile, liver function test, and kidney function test. Pathology reports are prepared after examining cells, tissues, or biopsy samples under a microscope and are very important in diagnosing diseases like cancer. Clinical or progress notes record how the patient is responding during treatment. A discharge summary is given when a patient leaves the hospital and includes diagnosis, treatment given, medicines, and follow-up advice. Operative reports are written after surgery and explain what procedure was done, what was observed, and whether any complications occurred. Prescription reports mention the medicines, dosage, timing, duration, and instructions given by the doctor.

Among all these, **medical imaging reports** are especially important because they are based on visual information from inside the body. These reports are usually written by radiologists after studying scans such as X-rays, CT scans, MRI scans, ultrasound, mammography, or PET scans. Medical imaging helps doctors look inside the body without performing surgery. It converts internal body structures into images, and the radiologist then interprets those images into a written report.

Different imaging methods are used for different purposes. **X-rays** are commonly used to detect bone fractures, joint dislocations, dental problems, and chest infections like pneumonia. **CT scans** use multiple X-ray images taken from different angles to create detailed cross-sectional views of the body. They are useful for internal injuries, tumors, lung problems, bleeding, and emergency trauma cases. **MRI scans** use magnetic fields and radio waves to create detailed images, especially of soft tissues such as the brain, spinal cord, muscles, ligaments, and joints. **Ultrasound** uses sound waves to produce real-time images and is commonly used in pregnancy, abdominal examination, heart imaging, and fluid assessment. **Mammography** is mainly used for breast screening, while **PET scans** help study metabolic activity, especially in cancer and neurological conditions.

A medical imaging report usually follows a proper structure. The first part includes **patient and exam details**, such as the patient information, date of scan, type of imaging test, and body part examined. The **clinical history or indication** explains why the scan was requested, for example headache, chest pain, injury, suspected fracture, abdominal pain, tumor evaluation, or follow-up of a previous condition. The **comparison** section mentions older scans if available, so the radiologist can check whether the condition has improved, worsened, or stayed stable. The **technique** section explains how the scan was performed, including whether contrast dye was used, what views were taken, or what protocol was followed. The **findings** section is the main descriptive part of the report. Here, the radiologist describes what is visible in the images, including normal structures and any abnormality such as fracture, swelling, infection, tumor, bleeding, fluid collection, or tissue damage. The final section is the **impression** or **conclusion**, which summarizes the most important findings and may suggest the likely diagnosis or next step.

Medical imaging reports are very useful because they support diagnosis, treatment planning, and follow-up. For example, an X-ray report can confirm a fracture, a CT report can detect internal injury, an MRI report can help evaluate a brain or spine problem, and an ultrasound report can show the condition of abdominal organs or pregnancy. These reports are also highly connected to computer vision and artificial intelligence. In AI for healthcare, models can be trained to analyze medical images and detect patterns such as tumors, fractures, pneumonia, diabetic retinopathy, or other abnormalities. However, AI is only an assisting tool. The final medical interpretation still needs doctors and radiologists because the report must be understood along with the patient’s symptoms, medical history, scan quality, and clinical context.

### References

* RadiologyInfo.org, “All About Your Radiology Report: What to Know”
* American College of Radiology, “Practice Parameter for Communication of Diagnostic Imaging Findings”
* RadiologyInfo.org, “How to Read Your Radiology Report”

