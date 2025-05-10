#load("@rules_python//python:defs.bzl", "py_binary")
py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    deps = [":hello_world_lib"],
    visibility = ["//visibility:public"],
)

py_library(
    name = "hello_world_lib",
    srcs = ["hello_world_lib.py"],
    visibility = ["//visibility:public"],
)
