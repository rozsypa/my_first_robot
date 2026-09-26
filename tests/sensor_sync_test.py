#simple assert test for sensor sync script
import math
from src.sensor_sync import interpolate_position
from src.sensor_sync import camera_time

test_data = [
    (1.00,0.50),
    (1.10,0.56)
]

assert(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.02),0.512,rel_tol=1e-09))
print(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],0.523),0.53,rel_tol=1e-09))
assert(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.02),0.512,rel_tol=1e-09))
print(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.02),0.512,rel_tol=1e-09))
assert(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.00),0.50,rel_tol=1e-09))
print(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.00),0.50,rel_tol=1e-09))
assert(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.10),0.56,rel_tol=1e-09))
print(math.isclose(interpolate_position(test_data[0][0],test_data[0][1],test_data[1][0],test_data[1][1],1.10),0.56,rel_tol=1e-09))
#edge cases

edge_test_data = [
    (1.00,0.50),
    (1.00,0.56)
]
assert(math.isclose(interpolate_position(edge_test_data[0][0],edge_test_data[0][1],edge_test_data[1][0],edge_test_data[1][1],1.10),0.56))
