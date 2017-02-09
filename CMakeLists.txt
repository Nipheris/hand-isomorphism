cmake_minimum_required(VERSION 3.0)

project(hand-isomorphism VERSION 0.1.0 LANGUAGES C)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
foreach(CONFIG ${CMAKE_CONFIGURATION_TYPES})
	string(TOUPPER ${CONFIG} UPPER_CONFIG)
	set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_${UPPER_CONFIG} ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY}/${CONFIG})
	set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_${UPPER_CONFIG} ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/${CONFIG})
	set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_${UPPER_CONFIG} ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${CONFIG})
endforeach(CONFIG CMAKE_CONFIGURATION_TYPES)

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

if(UNIX)
	set(CPACK_PACKAGE_NAME "lib${PROJECT_NAME}")
endif()
set(CPACK_PACKAGE_CONTACT "Stanislav Makarov <nipheris@live.ru>")
set(CPACK_PACKAGE_VENDOR "Kevin Waugh <waugh@cs.cmu.edu>")
set(CPACK_WIX_UPGRADE_GUID "{F5CFBC67-77D5-46E1-8E0E-760D4EDFDE1F}")
include(CPack)
