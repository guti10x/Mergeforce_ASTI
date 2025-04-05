# Mergeforce – Asti Robotic Challenge 25

Este repositorio contiene el diseño, la implementación y el código del robot autónomo **Mergeforce**, desarrollado para las semifinales del **Asti Robotic Challenge 25**. El objetivo del desafío fue construir un robot capaz de competir de forma autónoma en dos categorías:

---

## Categorías de Competencia

### Seguidor de Líneas

En esta modalidad, el robot debe seguir una línea trazada en el suelo, ajustando su trayectoria ante curvas o variaciones del circuito. Para ello, se emplean sensores infrarrojos que detectan la línea y permiten al robot mantenerse alineado.

![IMG_0143-_1_](https://github.com/user-attachments/assets/a3899a9c-c226-482b-b06d-81476d7c998a)

### Sumo

En esta categoría, el robot debe detectar y empujar a su oponente fuera de un área circular. Utiliza sensores ultrasónicos para medir distancias y calcular la mejor estrategia de empuje.

![IMG_0207](https://github.com/user-attachments/assets/7478ef8e-e708-44fc-a4f4-1fbdbd683c62)

---

## Componentes Utilizados

| Componente               | Función                                                               |
|--------------------------|-----------------------------------------------------------------------|
| **Raspberry Pi**         | Controlador principal y toma de decisiones de alto nivel              |
| **Arduino**              | Controlador de bajo nivel para sensores y actuadores                  |
| **PyFirmata4**           | Librería para la comunicación entre Raspberry Pi y Arduino            |
| **Sensores ultrasónicos**| Detección de distancia en la categoría de sumo                        |
| **Sensores infrarrojos** | Detección de la línea en el modo seguidor                             |
| **Motores DC**           | Propulsión y maniobras del robot                                      |

---

## Arquitectura del Sistema

El sistema del robot se basa en una arquitectura distribuida con dos unidades principales:

- **Raspberry Pi**: Se encarga de la lógica de alto nivel, incluyendo la toma de decisiones y el procesamiento de datos de los sensores.
- **Arduino**: Gestiona el control de motores y la lectura directa de sensores.
- La comunicación entre ambos se realiza a través del protocolo **PyFirmata4**, que permite el intercambio fluido de datos y comandos.

---

## Requisitos Técnicos

- **Python 3.x**
- **Arduino con firmware StandardFirmata cargado**
- **Librería PyFirmata4** (instalable con: `sudo pip3 install pymata4 --break-system-packages`)
