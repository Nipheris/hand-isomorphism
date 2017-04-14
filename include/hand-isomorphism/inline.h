#ifndef _INLINE_H_
#define _INLINE_H_

// if we are using VC++ 18.00 or lower,
// if we compile C code,
// and if no any macro named 'inline' is already defined
#if defined(_MSC_VER) && _MSC_VER <= 1800 && !defined(__cplusplus) && !defined(inline)
#define inline __inline
#endif

#endif // _INLINE_H_
