uniform float pot1; // #1
uniform float pot2; // #2
uniform float pot3; // #3
uniform float pot4; // #4

uniform bool btn_reset; // #5
uniform float enc_a; // #6
uniform float enc_b; // #7
uniform float enc_btn; // #8

uniform bool btn1; // #9
uniform bool btn2; // #10
uniform bool btn3; // #11
uniform bool btn4; // #12

uniform vec2 position; // <position> =(0.5,0.5)
uniform vec2 joy_l_xy; // <velocity> #13:14
uniform bool joy_l_z; // =0 #15

uniform vec2 orientation;
uniform vec2 joy_r_xy; // #16:17
uniform bool joy_r_z; // #18

void main() {
    vec2 p = gl_FragCoord.xy / Resolution;
    float aspect = Resolution.x / Resolution.y;
    p.x = (p.x - 0.5) * aspect + 0.5;

    vec2 center = vec2(0.5);
    vec3 color = vec3(0.);

    if (length(p - position.xy) < 0.1) {
        if (joy_l_z) {
            color = vec3(0.7,0.1,0.1);
        } else {
            color = vec3(1.);
        }
    }

    FragColor = vec4(color, 1.);
}
