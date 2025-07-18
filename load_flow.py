import pandapower as pp
import pandapower.plotting.plotly as plotly

# Buat jaringan kosong
net = pp.create_empty_network()

# Buat 16 bus distribusi (0.4 kV)
buses = []
for i in range(16):
    bus = pp.create_bus(net, vn_kv=0.4, name=f"Bus {i+1}")
    buses.append(bus)

# Tambahkan sumber di Bus 1 (Grid)
pp.create_ext_grid(net, bus=buses[0], vm_pu=1.0, name="Grid")

# Hubungkan bus secara radial menggunakan line
for i in range(15):  # 15 saluran dari Bus 1 ke Bus 16
    pp.create_line_from_parameters(
        net,
        from_bus=buses[i],
        to_bus=buses[i+1],
        length_km=0.1,               # 100 meter per line
        r_ohm_per_km=0.3,            # Resistansi realistis
        x_ohm_per_km=0.05,           # Reaktansi realistis
        c_nf_per_km=0,               # Abaikan kapasitansi untuk kesederhanaan
        max_i_ka=0.2,                # Arus maksimum 200 A
        name=f"Line {i+1}-{i+2}"
    )

# Tambahkan beban kecil di setiap bus (kecuali Bus 1 sebagai sumber)
for i in range(1, 16):
    pp.create_load(net, bus=buses[i], p_mw=0.01, q_mvar=0.002, name=f"Beban Bus {i+1}")

# Jalankan aliran daya
pp.runpp(net)

# Tampilkan hasil aliran daya
print(net.res_bus)
print(net.res_load)
print(net.res_ext_grid)

# Visualisasi jaringan dengan plotly
plotly.simple_plotly(net)
