uniform sampler2D texture;
uniform int width;

varying vec2 fragmentUV;

/*
* Convert from YUYV422 to RGB.
*
* This is used by MovieTexture_Generic.  The input texture is width
* texels wide, the output texture is width*2 texels wide, and texels
* are aligned.  We can use this to determine if the fragment we're generating
* is even or odd.
*/
void main(void)
{
    float fRealWidth = float(width);
    vec2 uv = fragmentUV;
    float fU = uv.x;

    /* Scale U to [0.25,fRealWidth+0.25]. */
    fU *= fRealWidth;

    /* Scale the U texture coordinate to the size of the destination texture,
    * [0.5,fDestWidth+0.5]. */
    fU *= 2.0;

    /* Texture coordinates are center-aligned; an exact sample lies at 0.5,
    * not 0.  Shift U from [0.5,fDestWidth+0.5] to [0,fDestWidth]. */
    fU -= 0.5;

    /* If this is an odd fragment, fOdd is 1. */
    float fOdd = mod(fU+0.0001, 2.0);


    /* Align fU to an even coordinate. */
    fU -= fOdd;

    /* Scale U back.  Because fU is aligned to an even coordinate, this
    * will always be an exact sample. */
    fU += 0.5;
    fU /= 2.0;
    fU /= fRealWidth;

    uv.x = fU;

    vec4 yuyv = texture2D( texture, uv );

    vec3 yuv;
    if( fOdd <= 0.5 )
        yuv = yuyv.rga;
    else
        yuv = yuyv.bga;
    yuv -= vec3(16.0/255.0, 128.0/255.0, 128.0/255.0);

    mat3 conv = mat3(
        // Y     U (Cb)    V (Cr)
        1.1643,  0.000,    1.5958,  // R
        1.1643, -0.39173, -0.81290, // G
        1.1643,  2.017,    0.000);  // B

    gl_FragColor.r=dot(yuv,conv[0]);
    gl_FragColor.g=dot(yuv,conv[1]);
    gl_FragColor.b=dot(yuv,conv[2]);
    gl_FragColor.a = 1.0;

    /* Why doesn't this work? */
    //      gl_FragColor.rgb = yuv * conv;
    //      gl_FragColor.a = 1.0;
}