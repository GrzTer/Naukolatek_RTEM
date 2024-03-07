# Documentación sobre RTEM
---
## (MZE) Monitorowanie Zużycia Energii:
Aplikacja Energy Consumption Monitoring została zaprojektowana w celu wykorzystania zaawansowanej technologii IoT do śledzenia i analizowania zużycia energii elektrycznej na różnych poziomach, od pojedynczych urządzeń po całe budynki. Wykorzystując Django do backendu, system jest zbudowany wokół kluczowych modeli, w tym Device, TemperatureMeasurement i VoltageMeasurement, które wspólnie ułatwiają gromadzenie, przechowywanie i analizę krytycznych parametrów, takich jak częstotliwość, rezystancja, napięcie i temperatura.

Każde urządzenie jest jednoznacznie identyfikowane przez numer seryjny, generowany automatycznie w celu zapewnienia unikalności i łatwości śledzenia. Modele TemperatureMeasurement i VoltageMeasurement są powiązane z konkretnymi urządzeniami, umożliwiając precyzyjne monitorowanie warunków środowiskowych i parametrów elektrycznych w czasie. Pomiary są opatrzone znacznikami czasu, zapewniając historyczną ścieżkę danych do analizy i optymalizacji zużycia energii.

Aplikacja obsługuje wielu użytkowników i budynków, dzięki czemu jest skalowalna zarówno dla nieruchomości mieszkalnych, jak i komercyjnych. Została zaprojektowana z myślą o możliwości rozbudowy, umożliwiając przyszłą integrację dodatkowych typów pomiarów i urządzeń IoT bez znaczącej restrukturyzacji.

Niniejsza dokumentacja ma na celu poprowadzenie deweloperów i administratorów systemu przez konfigurację, wdrażanie i codzienne zarządzanie aplikacją 'Monitorowanie Zużycia Energii', zapewniając solidne i przyjazne dla użytkownika doświadczenie w zakresie skutecznego monitorowania i zmniejszania zużycia energii.
