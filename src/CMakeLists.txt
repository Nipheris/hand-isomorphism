# Header and source files
file(GLOB HAND_ISOMORPHISM_PUBLIC_HEADERS ${PROJECT_SOURCE_DIR}/include/hand-isomorphism/*.h)
file(GLOB HAND_ISOMORPHISM_PRIVATE_HEADERS *.h)
file(GLOB HAND_ISOMORPHISM_SOURCES *.c)

# Group source files for IDE source explorers (e.g. Visual Studio)
source_group("Public Header Files" FILES ${HAND_ISOMORPHISM_PUBLIC_HEADERS})
source_group("Private Header Files" FILES ${HAND_ISOMORPHISM_PRIVATE_HEADERS})
source_group("Source Files" FILES ${HAND_ISOMORPHISM_SOURCES})

add_library(hand-isomorphism STATIC
	${HAND_ISOMORPHISM_PUBLIC_HEADERS}
	${HAND_ISOMORPHISM_PRIVATE_HEADERS}
	${HAND_ISOMORPHISM_SOURCES}
)
set_target_properties(hand-isomorphism PROPERTIES POSITION_INDEPENDENT_CODE ON)
set_target_properties(hand-isomorphism PROPERTIES PUBLIC_HEADER "${HAND_ISOMORPHISM_PUBLIC_HEADERS}")
target_include_directories(hand-isomorphism
	PUBLIC
		$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
		$<INSTALL_INTERFACE:include>
	PRIVATE
		${PROJECT_SOURCE_DIR}/include/hand-isomorphism
)

include(CheckFunctionExists)
CHECK_FUNCTION_EXISTS(log LOG_EXISTS)
if(NOT LOG_EXISTS)
	target_link_libraries(hand-isomorphism m)
endif()

#set_target_properties(hand-isomorphism PROPERTIES C_STANDARD 99)
# C_STANDARD target property is only available since CMake 3.1,
# so we need this workaround to enable C99 on GNU compiler
if(CMAKE_COMPILER_IS_GNUCC)
	target_compile_options(hand-isomorphism PUBLIC "--std=c99")
endif()

# Put "hand-isomorphism" target into a "hand-isomorphism" export-set
install(
	TARGETS hand-isomorphism
	EXPORT hand-isomorphism
	PUBLIC_HEADER DESTINATION include/hand-isomorphism
	ARCHIVE DESTINATION lib
	LIBRARY DESTINATION lib
)
