// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from battery_msg:msg/BatteryStatus.idl
// generated code does not contain a copyright notice

#ifndef BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__BUILDER_HPP_
#define BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "battery_msg/msg/detail/battery_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace battery_msg
{

namespace msg
{

namespace builder
{

class Init_BatteryStatus_temperature
{
public:
  explicit Init_BatteryStatus_temperature(::battery_msg::msg::BatteryStatus & msg)
  : msg_(msg)
  {}
  ::battery_msg::msg::BatteryStatus temperature(::battery_msg::msg::BatteryStatus::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return std::move(msg_);
  }

private:
  ::battery_msg::msg::BatteryStatus msg_;
};

class Init_BatteryStatus_current
{
public:
  explicit Init_BatteryStatus_current(::battery_msg::msg::BatteryStatus & msg)
  : msg_(msg)
  {}
  Init_BatteryStatus_temperature current(::battery_msg::msg::BatteryStatus::_current_type arg)
  {
    msg_.current = std::move(arg);
    return Init_BatteryStatus_temperature(msg_);
  }

private:
  ::battery_msg::msg::BatteryStatus msg_;
};

class Init_BatteryStatus_voltage
{
public:
  Init_BatteryStatus_voltage()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BatteryStatus_current voltage(::battery_msg::msg::BatteryStatus::_voltage_type arg)
  {
    msg_.voltage = std::move(arg);
    return Init_BatteryStatus_current(msg_);
  }

private:
  ::battery_msg::msg::BatteryStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::battery_msg::msg::BatteryStatus>()
{
  return battery_msg::msg::builder::Init_BatteryStatus_voltage();
}

}  // namespace battery_msg

#endif  // BATTERY_MSG__MSG__DETAIL__BATTERY_STATUS__BUILDER_HPP_
