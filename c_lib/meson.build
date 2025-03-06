project('c_lib', 'c')

ed25519_sources = files(
  'ed25519/src/add_scalar.c',
  'ed25519/src/fe.c',
  'ed25519/src/ge.c',
  'ed25519/src/key_exchange.c',
  'ed25519/src/keypair.c',
  'ed25519/src/sc.c',
  'ed25519/src/seed.c',
  'ed25519/src/sha512.c',
  'ed25519/src/sign.c',
  'ed25519/src/verify.c',
)

static_library('ed25519', ed25519_sources, install: true)

static_library('json', 'json.c', include_directories: 'json.h', install: true)
