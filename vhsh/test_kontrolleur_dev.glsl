uniform float rot; // =0.5 #1
// uniform float x; // =0.5 #3
// uniform float y; // =0.5 #2
uniform vec2 position; // <position> =(0,0) [-1.,1.,0.1] #3:2
uniform float z; // =0. #4
uniform float distance; // #5


void main() {
    vec2 p = gl_FragCoord.xy / Resolution;
    float aspect = Resolution.x / Resolution.y;
    p.x = (p.x - 0.5) * aspect + 0.5;

    vec2 center = vec2(0.5);

    vec3 color = vec3(sin(p.x*6/distance + Time));

    // vec3 position = vec3(x, y, z);
    if (length(p - position.xy) < rot) {
        if (z > 0.5) {
            color = vec3(0.7,0.1,0.1);
        } else {
            color = vec3(1.);
        }
    }

    FragColor = vec4(color, 1.);
}
