cmake_minimum_required(VERSION 3.0)

project(hand-isomorphism VERSION 0.1.0 LANGUAGES C)

add_subdirectory(src)
add_subdirectory(tests)

set(CMAKECONFIG_INSTALL_DIR "share/hand-isomorphism")

include(CMakePackageConfigHelpers)
configure_package_config_file(
	"hand-isomorphism-config.cmake.in"
	"hand-isomorphism-config.cmake"
	INSTALL_DESTINATION ${CMAKECONFIG_INSTALL_DIR} # install destination should match with the one used in install command below
)
write_basic_package_version_file(
	"hand-isomorphism-config-version.cmake"
	VERSION 0.1.0
	COMPATIBILITY SameMajorVersion
)

# Export targets from "hand-isomorphism" export-set to be used from build directory
export(
	EXPORT hand-isomorphism
	FILE "hand-isomorphism-targets.cmake"
)
# Publish build directory to the package registry
export(PACKAGE hand-isomorphism)

# Install targets from "hand-isomorphism" export-set
install(
	EXPORT hand-isomorphism
	FILE "hand-isomorphism-targets.cmake"
	DESTINATION ${CMAKECONFIG_INSTALL_DIR}
)
# Install generated package config and version files
install(
	FILES "${CMAKE_CURRENT_BINARY_DIR}/hand-isomorphism-config.cmake" "${CMAKE_CURRENT_BINARY_DIR}/hand-isomorphism-config-version.cmake"
	DESTINATION ${CMAKECONFIG_INSTALL_DIR}
)
