# playtennis-regression
Machine Learning-7

Bu uygulama, hava durumu koşullarına bağlı olarak tenis oynamanın olasılığını tahmin etmek için bir Python programıdır.

## Veriler

Veriler, "tenis_veriler.csv" adlı bir veri dosyasından okunur. Bu veri dosyası hava durumu koşulları (örneğin, yağmur, güneş, rüzgar) ve sıcaklık gibi bağımsız değişkenlerle birlikte tenis oynama kararını içerir.

## Veri Ön İşleme

Veri ön işleme adımları şunları içerir:
- Kategorik veriler Label Encoding ile dönüştürülür.
- Bazı kategorik veriler One-Hot Encoding ile dönüştürülür.
- Veriler birleştirilerek "sonveriler" adlı bir DataFrame oluşturulur.

## Linear Regression

Lineer regresyon yöntemi kullanılarak hava durumu faktörleri ile tenis oynama arasındaki ilişki modellenir. İş akışı aşağıdaki adımları içerir:
- Veri, eğitim ve test verilere bölünür.
- Bir Linear Regression modeli oluşturulur ve eğitilir.
- Model, test verileri üzerinde tahminler yapar ve sonuçlar kaydedilir.

## İstatistiksel Analiz

"statsmodels" kütüphanesi kullanılarak istatistiksel analiz yapılır. Modelin istatistiksel özeti görüntülenir.

## Gereksiz Sütunların Kaldırılması

Veri setinden gereksiz sütunlar kaldırılır.

## Tekrar Linear Regression

Tekrar bir Linear Regression modeli oluşturulur ve eğitilir.

## Nasıl Kullanılır

Bu uygulamayı çalıştırmak için aşağıdaki adımları izleyin:
1. Python'u yükleyin (https://www.python.org/downloads/).
2. Gerekli kütüphaneleri yüklemek için terminale komutları girin.
3. 3. "tenis_veriler.csv" dosyasını aynı dizine koyun veya kod içindeki dosya yolunu güncelleyin.
4. Kodu çalıştırın ve sonuçları gözlemleyin.



