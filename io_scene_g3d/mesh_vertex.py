#################################################################################
# Copyright 2014 See AUTHORS file.
#
# Licensed under the GNU General Public License Version 3.0 (the "LICENSE");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.gnu.org/licenses/gpl-3.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#################################################################################

from mathutils import Vector, Color

class MeshVertex:
    """Represents a vertex we can export, with facilities to compare two of them"""
    
    _position = None
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,position):
        if not isinstance(position, Vector):
            raise TypeError("position needs to be a mathutils.Vector")
        self._position = position
    
    _normal = None
    @property
    def normal(self):
        return self._normal
    @normal.setter
    def normal(self,normal):
        if not isinstance(normal, Vector):
            raise TypeError("normal needs to be a mathutils.Vector")
        self._normal = normal
        
    _tangent = None
    @property
    def tangent(self):
        return self._tangent
    @tangent.setter
    def tangent(self,tangent):
        if tangent != None and not isinstance(tangent, Vector):
            raise TypeError("tangent needs to be a mathutils.Vector")
        self._tangent = tangent
    
    _binormal = None
    @property
    def binormal(self):
        return self._binormal
    @binormal.setter
    def binormal(self,binormal):
        if binormal != None and not isinstance(binormal, Vector):
            raise TypeError("binormal needs to be a mathutils.Vector")
        self._binormal = binormal
    
    _texcoord = None
    @property
    def texcoord(self):
        return self._texcoord
    @texcoord.setter
    def texcoord(self,texcoord):
        if texcoord != None and not isinstance(texcoord, list):
            raise TypeError("texcoord needs to be a list of vectors (mathutils.Vector) or None")
        self._texcoord = texcoord
    
    _blendweight = None
    @property
    def blendweight(self):
        return self._blendweight
    @blendweight.setter
    def blendweight(self,blendweight):
        if blendweight != None and not isinstance(blendweight, list):
            raise TypeError("blendweight needs to be a list of vectors (mathutils.Vector) or None")
        self._blendweight = blendweight
    
    def __init__(self, position, normal, tangent = None, binormal = None, texcoord = None, blendweight = None):
        self.position = position
        self.normal = normal
        self.tangent = tangent
        self.binormal = binormal
        self.texcoord = texcoord
        self.blendweight = blendweight
        
    _color = None
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        if not isinstance(color, Color):
            raise TypeError("color needs to be a mathutils.Color")
        self._color = color
        
    def compare(self, another):
        """Compare two vertices, return True if they have the same value for all fields"""
        if another == None or not isinstance(another, MeshVertex):
            return False
        
        comparison = self.position == another.position \
                     and self.normal == another.normal \
                     and self.color == another.color \
                     and self.tangent == another.tangent \
                     and self.binormal == another.binormal \
                     and self.texcoord == another.texcoord \
                     and self.blendweight == another.blendweight
                     
        return comparison

    def normalize_weights(self):
        """Normalize all bone weights in this vertex so that they all sum to 1 (one)."""
        if self.blendweight != None:
            total_weight = 0.0
            for weight in self.blendweight:
                total_weight = total_weight + weight[1]
            
            if total_weight != 0.0:
                for weight in self.blendweight:
                    weight[1] = weight[1] / total_weight