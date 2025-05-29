// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from battery_msg:msg/BatteryStatus.idl
// generated code does not contain a copyright notice
#include "battery_msg/msg/detail/battery_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
battery_msg__msg__BatteryStatus__init(battery_msg__msg__BatteryStatus * msg)
{
  if (!msg) {
    return false;
  }
  // voltage
  // current
  // temperature
  return true;
}

void
battery_msg__msg__BatteryStatus__fini(battery_msg__msg__BatteryStatus * msg)
{
  if (!msg) {
    return;
  }
  // voltage
  // current
  // temperature
}

bool
battery_msg__msg__BatteryStatus__are_equal(const battery_msg__msg__BatteryStatus * lhs, const battery_msg__msg__BatteryStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // voltage
  if (lhs->voltage != rhs->voltage) {
    return false;
  }
  // current
  if (lhs->current != rhs->current) {
    return false;
  }
  // temperature
  if (lhs->temperature != rhs->temperature) {
    return false;
  }
  return true;
}

bool
battery_msg__msg__BatteryStatus__copy(
  const battery_msg__msg__BatteryStatus * input,
  battery_msg__msg__BatteryStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // voltage
  output->voltage = input->voltage;
  // current
  output->current = input->current;
  // temperature
  output->temperature = input->temperature;
  return true;
}

battery_msg__msg__BatteryStatus *
battery_msg__msg__BatteryStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  battery_msg__msg__BatteryStatus * msg = (battery_msg__msg__BatteryStatus *)allocator.allocate(sizeof(battery_msg__msg__BatteryStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(battery_msg__msg__BatteryStatus));
  bool success = battery_msg__msg__BatteryStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
battery_msg__msg__BatteryStatus__destroy(battery_msg__msg__BatteryStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    battery_msg__msg__BatteryStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
battery_msg__msg__BatteryStatus__Sequence__init(battery_msg__msg__BatteryStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  battery_msg__msg__BatteryStatus * data = NULL;

  if (size) {
    data = (battery_msg__msg__BatteryStatus *)allocator.zero_allocate(size, sizeof(battery_msg__msg__BatteryStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = battery_msg__msg__BatteryStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        battery_msg__msg__BatteryStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
battery_msg__msg__BatteryStatus__Sequence__fini(battery_msg__msg__BatteryStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      battery_msg__msg__BatteryStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

battery_msg__msg__BatteryStatus__Sequence *
battery_msg__msg__BatteryStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  battery_msg__msg__BatteryStatus__Sequence * array = (battery_msg__msg__BatteryStatus__Sequence *)allocator.allocate(sizeof(battery_msg__msg__BatteryStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = battery_msg__msg__BatteryStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
battery_msg__msg__BatteryStatus__Sequence__destroy(battery_msg__msg__BatteryStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    battery_msg__msg__BatteryStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
battery_msg__msg__BatteryStatus__Sequence__are_equal(const battery_msg__msg__BatteryStatus__Sequence * lhs, const battery_msg__msg__BatteryStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!battery_msg__msg__BatteryStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
battery_msg__msg__BatteryStatus__Sequence__copy(
  const battery_msg__msg__BatteryStatus__Sequence * input,
  battery_msg__msg__BatteryStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(battery_msg__msg__BatteryStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    battery_msg__msg__BatteryStatus * data =
      (battery_msg__msg__BatteryStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!battery_msg__msg__BatteryStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          battery_msg__msg__BatteryStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!battery_msg__msg__BatteryStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
