#define THRUST_DEVICE_SYSTEM THRUST_DEVICE_SYSTEM_OMP
#define libcloudphxx_particles_device omp
#define libcloudphxx_particles_real_t float // TODO: other?
#include "particles.ipp"