
# MAXIMOS
1. IN=2GHz (2*LO)
2. CLK=BW SPLITQ
3. OUT=2GHz (2*LO)

---------------------------------------------

# ESPECIFICACIONES: Plan de mediciones

## Aislacion LO/FI (pl1)
* HP 8350B: start: 500MHz - stop: 1.5GHz
* time: 10ms - pwr: 10/15/20dBm (rehacer para 5/10/15)

* Medicion: AislLO (I/Q)

Datos tomados: Imagenes/csv

-----------------------------------------------

## Aislacion RF/FI (pl1)
* HP 8350B: start: 0GHz - stop: 1.5GHz
* time: 10ms - pwr: 10/15/20dBm (rehacer para 5/10/15)

* Medicion: AislRF (I/Q)

Datos tomados: Imagenes/csv

-----------------------------------------------

## Aislacion LO/RF (pl1)
* HP 8350B: fc: 1GHz.
* pwr: 5/10/15dBm.

* Medicion: Att LO/RF (pwrLO-pwrRF), canales I,Q, Promediado para 5,10,15dBm.

### Att
1. Para 5dBm:  5-(-43.5)=48.5dB 
2. Para 10dBm: 10-(-40)=50dB
3. Para 15dBm: 15-(-39.2)=54.3dB

Promedio : 50.9 dB

---------------------------------------

## SPLITER-QUAD *(BW: 675-1300MHz)* (pl2)
* HP 8350B: start: 675MHz - stop: 1.3GHz.
* time: 10ms - pwr: 5/10/15dBm.

* Resp: Cos1
* AttMedia: 3.4dB aprox.

* Resp: Sin1
* AttMedia: 3.5aprox.

Datos tomados: csv/graficos python.

-----------------------------------------------

## MIXER-CONVLOSS *(BW: 675-1300MHz)*
* HP 8350B: start: 675MHz - stop: 1.3GHz.
* time: 10ms - pwr: 5/10/15dBm.
* RIGOL DSA815

* Resp: Cos1
* AttMedia: 3.4dB aprox.

* Resp: Sin1
* AttMedia: 3.5aprox.

Datos tomados: csv/graficos python.

----------------------------

## INVERSO(Sin LO) FI/RF (pl1)
* HP 8350B: 100/200/300MHz.
* pwr: 5/10/15dBm.
* RIGOL 

Datos tomados: Imagenes/Tabla de arm.