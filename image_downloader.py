from icrawler.builtin import BaiduImageCrawler
import os
import time

modelos = {
    "ax7": "东风风神AX7",
    "yixuan": "东风风神奕炫",
    "haoji": "东风风神皓极",
    "t5": "东风风行T5",
    "t5_evo": "东风风行T5 EVO",
    "lingzhi_m5": "东风风行菱智M5",
    "fengguang_580": "东风风光580",
    "fengguang_500": "东风风光500",
    "s560": "东风风光S560",
    "nammi_box": "东风纳米BOX",
    "epi_007": "东风奕派eπ007",
    "m_hero_917": "猛士917"
}

RAIZ = "dataset_dongfengo"

for carpeta, busqueda in modelos.items():
    ruta_destino = os.path.join(RAIZ, carpeta)
    os.makedirs(ruta_destino, exist_ok=True)

    print(f"Descargando: {busqueda} -> {ruta_destino}")

    # Crear el crawler sin filtros aquí
    crawler = BaiduImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': ruta_destino}
    )

    # Los filtros van en el método crawl
    crawler.crawl(keyword=busqueda, max_num=300, filters={'size': 'large'})

    # Pequeña pausa para no saturar (opcional)
    time.sleep(2)

print("¡Descarga completada!")