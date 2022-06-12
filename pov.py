import numpy as np

class Vector:
    
    def __init__(self, x, y, z):
        self.v = np.array((x, y, z))
        
    def __add__(self, other):
        v_sum = self.v + other.v
        return type(self)(*v_sum)
    
    def __neg__(self):
        return -1 * self
    
    def __sub__(self, other):
        v = self.v + (-other.v)
        return type(self)(*v)
                      
    def __mul__(self, scalar):
        v = scalar * self.v
        return type(self)(*v)
    
    # scalar on the left: s * Vector -> Vector.__rmul__(s)
    __rmul__ = __mul__
    
    def __truediv__(self, scalar):
        new_v = (1/scalar) * self.v
        return type(self)(*new_v)
    
    def normalize(self):
        if self.length != 0:
            return type(self)(*(self.v/self.length))
        else:
            return type(self)((0,0,0))
    
    @property
    def length(self):
        x, y, z = self.v
        return np.sqrt(sum((x**2, y**2, z**2)))
    
    def copy(self):
        return type(self)(*self.v)
    
    def __repr__(self):
        return 'Vector({},{},{})'.format(*self.v)
    
class POV_Vector(Vector):

    vert_template = ("sphere {{ {}, {} texture "
                     "{{ pigment {{ color {} }} }} no_shadow }}") 

    edge_template = ("cylinder {{ {}, {}, {} texture "
                     "{{pigment {{ color {} }} }} no_shadow }}")
        
    def draw_vert(self, c, r, outfile): 
        vert = "< {}, {}, {} >".format(*self.v)
        print(self.vert_template.format(vert, r, c), file=outfile)
        
    def draw_edge(self, c, r, outfile=None):
        v0_t = "< {}, {}, {} >".format(*(0,0,0))
        v1_t = "< {}, {}, {} >".format(*self.v)
        data = (v0_t, v1_t, r, c)
        print(self.edge_template.format(*data), file=outfile)

    def __repr__(self):
        return 'POV_Vector({},{},{})'.format(*self.v)

class POV_Edge:
    
    template = ("cylinder {{ {}, {}, {} texture "
                "{{pigment {{ color {} }} }} no_shadow }}")
        
    def __init__(self, v0, v1):
        self.v0 = v0
        self.v1 = v1
        
    def draw_edge(self, c, r, outfile=None):
        v = self.v0
        v0_t = "< {}, {}, {} >".format(*self.v0.v)
        v = self.v1
        v1_t = "< {}, {}, {} >".format(*self.v1.v)
        data = (v0_t, v1_t, r, c)
        print(self.template.format(*data), file=outfile)
            
    def __repr__(self):
        return "POV_Edge({}, {})".format(self.v0, self.v1)
        
class Polyhedron:
    
    def _distill(self):

        edges = []
        unique = set()
        
        for f in self.faces:
            for pair in zip(f , f[1:] + (f[0],)):
                unique.add( tuple(sorted(pair)) )
        
        for edge in unique:
            edges.append( POV_Edge(self.vertexes[edge[0]],
                                   self.vertexes[edge[1]]) )

        return edges            
         
    def render(self, output):
        for e in self.edges:
            e.draw_edge(c=self.edge_color, r=self.edge_radius, outfile=output)
        for v in self.vertexes.values():
            v.draw_vert(c=self.vert_color, r=self.vert_radius, outfile=output)
            
class Tetrahedron(Polyhedron):

    def __init__(self, verts):
        self.vertexes = verts
        self.faces = (('a','b','c'), 
                      ('a','c','d'), 
                      ('a','d','b'), 
                      ('b','c','d'))
        self.edges = self._distill()
        
        # POV-Ray
        self.edge_color = "rgb <1, 0.4, 0>"
        self.edge_radius= 0.03
        self.vert_color = "rgb <1, 0.4, 0>"
        self.vert_radius= 0.05


class InvTetrahedron(Polyhedron):
    """
    Inverse Tetrahedron
    """
    
    def __init__(self, verts):
        
        self.vertexes = verts
        self.faces = (('e','f','g'),
                      ('e','g','h'),
                      ('e','h','f'),
                      ('f','h','g'))
        self.edges = self._distill()
        
        # POV-Ray
        self.edge_color = "rgb <0, 0, 0>" # black
        self.edge_radius= 0.03
        self.vert_color = "rgb <0, 0, 0>" # black
        self.vert_radius= 0.05
        
class Cube (Polyhedron):
    """
    Cube
    """

    def __init__(self, verts):
        self.vertexes = verts        
        self.faces = (('a','f','c','h'),
                      ('h','c','e','b'),
                      ('b','e','d','g'),
                      ('g','d','f','a'),
                      ('c','f','d','e'),
                      ('a','h','b','g'))
        self.edges = self._distill()
 
        # POV-Ray
        self.edge_color = "rgb <0, 1, 0>"
        self.edge_radius= 0.03
        self.vert_color = "rgb <0, 1, 0>"
        self.vert_radius= 0.03


class Octahedron (Polyhedron):
    """
    Octahedron
    """

    def __init__(self, verts):

        self.vertexes = verts
        self.faces = (('j','k','i'),('j','i','l'),('j','l','n'),('j','n','k'),               
                      ('m','k','i'),('m','i','l'),('m','l','n'),('m','n','k'))

        self.edges = self._distill()        
        # POV-Ray
        self.edge_color = "rgb <1, 0, 0>"
        self.edge_radius= 0.03
        self.vert_color = "rgb <1, 0, 0>"
        self.vert_radius= 0.03

pov_header = """
// Persistence of Vision Ray Tracer Scene Description File
// File: xyz.pov
// Vers: 3.6
// Desc: test file
// Date: Sat Sep  7 09:49:33 2019
// Auth: me
// ==== Standard POV-Ray Includes ====

#include "colors.inc"     // Standard Color definitions

// include "textures.inc"   // Standard Texture definitions
// include "functions.inc"  // internal functions usable in user defined functions

// ==== Additional Includes ====
// Don't have all of the following included at once, it'll cost memory and time
// to parse!
// --- general include files ---
// include "chars.inc"      // A complete library of character objects, by Ken Maeno

#include "skies.inc"      // Ready defined sky spheres

// include "stars.inc"      // Some star fields
// include "strings.inc"    // macros for generating and manipulating text strings

// --- textures ---
// include "finish.inc"     // Some basic finishes
// include "glass.inc"      // Glass textures/interiors
// include "golds.inc"      // Gold textures
// include "metals.inc"     // Metallic pigments, finishes, and textures
// include "stones.inc"     // Binding include-file for STONES1 and STONES2
// include "stones1.inc"    // Great stone-textures created by Mike Miller
// include "stones2.inc"    // More, done by Dan Farmer and Paul Novak
// include "woodmaps.inc"   // Basic wooden colormaps
// include "woods.inc"      // Great wooden textures created by Dan Farmer and Paul Novak

global_settings {assumed_gamma 1.0}
global_settings {ambient_light rgb<1, 1, 1> }

// perspective (default) camera
camera {
  location  <4, 0.1, 0.2>
//  rotate    <45, 45, 0.0>
  look_at   <0.0, 0.0,  0.0>
  right     x*image_width/image_height
}

// create a regular point light source
light_source {
  0*x                  // light's position (translated below)
  color rgb <1,1,1>    // light's color
  translate <-20, 15, 10>
}

// create a regular point light source
light_source {
  0*x                  // light's position (translated below)
  color rgb <1,1,1>    // light's color
  translate <20, -15, -10>
}

sky_sphere {S_Cloud2}
"""

if __name__ == "__main__":
    # Tetrahedron
    a = POV_Vector(x =  0.35355339059327373, 
                   y =  0.35355339059327373, 
                   z =  0.35355339059327373)

    b = POV_Vector(x = -0.35355339059327373, 
                   y = -0.35355339059327373, 
                   z =  0.35355339059327373)

    c = POV_Vector(x = -0.35355339059327373, 
                   y =  0.35355339059327373, 
                   z = -0.35355339059327373)

    d = POV_Vector(x =  0.35355339059327373, 
                   y = -0.35355339059327373, 
                   z = -0.35355339059327373)
    
    e,f,g,h     = b+c+d, a+c+d, a+b+d, a+b+c 
    i,j,k,l,m,n = a+b, a+c, a+d, b+c, b+d, c+d
    
    t_dict    = {'a':a, 'b':b, 'c':c, 'd':d}
    it_dict   = {'e':e, 'f':f, 'g':g, 'h':h}
    cube_dict = t_dict.copy()
    cube_dict.update(it_dict)
    octa_dict = {'i':i, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n}
    
    t  = Tetrahedron(t_dict)
    it = InvTetrahedron(it_dict)
    c  = Cube(cube_dict)
    oc = Octahedron(octa_dict)
    
    with open("render_me.pov", 'w') as output:
        print(pov_header, file=output)
        t.render(output)
        it.render(output)
        c.render(output)
        oc.render(output)