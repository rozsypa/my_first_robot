// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from battery_msg:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

#ifndef BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__STRUCT_H_
#define BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/BatteryStatus in the package battery_msg.
typedef struct battery_msg__msg__BatteryStatus
{
  float voltage;
  float current;
  float temperature;
} battery_msg__msg__BatteryStatus;

// Struct for a sequence of battery_msg__msg__BatteryStatus.
typedef struct battery_msg__msg__BatteryStatus__Sequence
{
  battery_msg__msg__BatteryStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} battery_msg__msg__BatteryStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__STRUCT_H_
