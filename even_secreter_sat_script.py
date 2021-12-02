from skyfield.api import Topos, load
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

ts = load.timescale()

def timeline(start, duration, step):
    return ts.utc(*[*start.utc][:4], start.utc[4] + range(0, duration, step))

def plot_point(ax, p, t, fmt, transform):
    sp = p.subpoint()
    coords = (sp.longitude.degrees, sp.latitude.degrees)

    ax.plot(*coords, fmt + 'o')
    # ax.text(*coords, t.utc_strftime(), 
    #      rotation=-30, ha= 'left', va = 'top')

def sat_track(ax, satellite, fmt, starttime, duration=240, time_step=1, transform=ccrs.PlateCarree()):
    print("top secret!")
    for t in timeline(starttime, duration, time_step):
        p = satellite.at(t)
        plot_point(ax, p, t, fmt, transform)
    ax.plot()

if __name__ == "__main__":
    pass
