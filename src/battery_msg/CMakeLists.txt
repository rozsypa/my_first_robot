cmake_minimum_required(VERSION 3.8)
project(battery_msg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(battery_msg REQUIRED)		# <-- přidáno
find_package(rosidl_default_generators REQUIRED)  # <-- přidáno

# přidání generování zpráv
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BatteryStatus.msg"  # <-- uprav podle tvého názvu souboru
  DEPENDENCIES std_msgs
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
