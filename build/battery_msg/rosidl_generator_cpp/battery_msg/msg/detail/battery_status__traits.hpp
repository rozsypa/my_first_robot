// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from battery_msg:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

#ifndef BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__TRAITS_HPP_
#define BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "battery_msg/msg/detail/battery_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace battery_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const BatteryStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: voltage
  {
    out << "voltage: ";
    rosidl_generator_traits::value_to_yaml(msg.voltage, out);
    out << ", ";
  }

  // member: current
  {
    out << "current: ";
    rosidl_generator_traits::value_to_yaml(msg.current, out);
    out << ", ";
  }

  // member: temperature
  {
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BatteryStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: voltage
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "voltage: ";
    rosidl_generator_traits::value_to_yaml(msg.voltage, out);
    out << "\n";
  }

  // member: current
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current: ";
    rosidl_generator_traits::value_to_yaml(msg.current, out);
    out << "\n";
  }

  // member: temperature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BatteryStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace battery_msg

namespace rosidl_generator_traits
{

[[deprecated("use battery_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const battery_msg::msg::BatteryStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  battery_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use battery_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const battery_msg::msg::BatteryStatus & msg)
{
  return battery_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<battery_msg::msg::BatteryStatus>()
{
  return "battery_msg::msg::BatteryStatus";
}

template<>
inline const char * name<battery_msg::msg::BatteryStatus>()
{
  return "battery_msg/msg/BatteryStatus";
}

template<>
struct has_fixed_size<battery_msg::msg::BatteryStatus>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<battery_msg::msg::BatteryStatus>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<battery_msg::msg::BatteryStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__TRAITS_HPP_
