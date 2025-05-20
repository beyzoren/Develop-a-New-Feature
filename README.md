# 📦 Shortest Path Python Package – shortestpath2200674010

Bu proje, **GMT211 Veri Yapıları ve Algoritmalar** dersi kapsamında geliştirilmiş olup, Python dilinde yazılmış bir **Dijkstra algoritması uygulamasını** içerir.  
Kodlar bir Python paketi haline getirilmiş, `pytest` ile test edilmiş, `Sphinx` ile dökümantasyonu oluşturulmuş ve **TestPyPI** ortamına başarıyla yüklenmiştir.  
Ek olarak, **GitHub Actions** entegrasyonu sağlanarak Continuous Integration (CI) otomasyonu gerçekleştirilmiştir.

---

## 🧭 Proje Amacı

Bu proje ile amaçlanan:

- En kısa yol probleminin çözümünde Dijkstra algoritmasının Python ile uygulanması,
- Bu algoritmanın bir **Python paketi** haline getirilmesi,
- Otomatik test mekanizmalarının kurulması (pytest & GitHub Actions),
- Paketleme, dökümantasyon ve yükleme süreçlerinin uçtan uca gerçekleştirilmesidir.

---

## 📁 Proje Klasör Yapısı

```plaintext
shortestpath_package/
├── shortestpath/                  # Ana modül (algoritma burada)
│   ├── __init__.py
│   └── shortestpath.py
│
├── tests/                         # pytest test dosyaları
│   └── test_shortestpath.py
│
├── docs/                          # Sphinx dökümantasyonu
│   └── build/html/index.html
│
├── .github/workflows/            # GitHub Actions dosyası
│   └── python-test.yml
│
├── setup.py                      # Paket yapılandırma dosyası
├── requirements.txt              # Gerekli kütüphaneler
├── README.md                     # Bu dosya
└── dist/                         # Oluşturulan .tar.gz ve .whl dosyaları

🚀 Paket Kurulumu (TestPyPI Üzerinden)
bash
Kopyala
Düzenle
pip install -i https://test.pypi.org/simple/ shortestpath2200674051
📦 Paket sayfası:
🔗 https://test.pypi.org/project/shortestpath2200674051/

🧠 Kullanım Örneği
python
Kopyala
Düzenle
from shortestpath.shortestpath import dijkstra

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

result = dijkstra(graph, 'A')
print(result)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
🧪 Otomatik Testler
Testler pytest ile yazılmıştır. tests/test_shortestpath.py içerisinde basit bir yönlü grafikte beklenen sonuçlar kontrol edilmiştir.

Testleri çalıştırmak için terminalde:

bash
Kopyala
Düzenle
pytest
📚 Dökümantasyon (Sphinx)
Sphinx ile oluşturulan dökümantasyon docs/build/html/index.html konumunda yer alır. Tarayıcıdan açılarak görsel olarak incelenebilir.

Dokümantasyon örneği:

Fonksiyon açıklamaları

Parametre tipleri

Geri dönen değerler

⚙️ GitHub Actions Entegrasyonu
.github/workflows/python-test.yml dosyası sayesinde her push sonrası GitHub otomatik olarak:

pip install -r requirements.txt komutu ile bağımlılıkları yükler

pytest ile testleri çalıştırır

Bu sayede sürekli entegrasyon (CI) sağlanmış olur.
✅ Workflow sonuçları “Actions” sekmesinden takip edilebilir.

🧾 Kullanılan Teknolojiler
Python 3.10

heapq (öncelik kuyruğu kullanımı)

Pytest

Sphinx

GitHub Actions

setuptools, twine

TestPyPI

👩‍💻 Geliştirici Bilgisi
Adı: Beyza Ören

Öğrenci No: 2200674051

E-posta: beyzaoren58@hotmail.com

Kapsam: GMT211 – Python Paket Geliştirme Ödevi

📌 Notlar
Bu proje yalnızca eğitim amacıyla TestPyPI’ye yüklenmiştir.

Gerçek ortam için yükleme yapılmamıştır.

Geliştirme sırasında tüm adımlar (build, twine upload, sphinx, pytest, CI) başarıyla test edilmiştir.


