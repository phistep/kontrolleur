uniform float pot_1; // #knob1
uniform float pot_2; // #knob2
uniform float pot_3; // #knob3
uniform float pot_4; // #knob4

uniform bool btn_reset; // #5

uniform float enc_a; // #6
uniform float enc_b; // #7
uniform bool enc_btn; // #8

uniform bool btn_1; // #button1
uniform bool btn_2; // #button2
uniform bool btn_3; // #button3
uniform bool btn_4; // #button4

uniform vec2 position; // <position> =(0.5,0.5)
uniform vec2 joy_l_xy; // <velocity> #joyLX:joyLY
uniform bool joy_l_z; // =0 #joyLZ

uniform vec2 orientation;
uniform vec2 joy_r_xy; // #joyRX:joyRY
uniform bool joy_r_z; // =0 #joyRZ

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
