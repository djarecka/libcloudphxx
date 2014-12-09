import sys
sys.path.insert(0, "../../bindings/python/")

from numpy import array as arr_t # ndarray dtype default to float64, while array's is int64!

from libcloudphxx import blk_1m

opts = blk_1m.opts_t()
print "cond =", opts.cond
print "cevp =", opts.cevp
print "revp =", opts.revp 
print "conv =", opts.conv 
print "accr =", opts.accr 
print "sedi =", opts.sedi 
print "r_c0 =", opts.r_c0
print "r_eps =", opts.r_eps

rhod = arr_t([1.  ])
th   = arr_t([300.])
rv   = arr_t([0.  ])
rc   = arr_t([0.01])
rr   = arr_t([0.  ])
dt   = 1
dz   = 1

th_old = th.copy()
rv_old = rv.copy()
rc_old = rc.copy()
rr_old = rr.copy()
blk_1m.adj_cellwise(opts, rhod, th, rv, rc, rr, dt)
assert th != th_old # some water should have evaporated
assert rv != rv_old
assert rc != rc_old
assert rr == rr_old

dot_rc = arr_t([0.])
dot_rr = arr_t([0.])
blk_1m.rhs_cellwise(opts, dot_rc, dot_rr, rc, rr)
assert dot_rc != 0 # some water should have coalesced
assert dot_rr != 0

dot_rr_old = dot_rr.copy()
flux = blk_1m.rhs_columnwise(opts, dot_rr, rhod, rr, dz)
assert flux == 0
assert dot_rr == dot_rr_old # no rain water -> no precip
