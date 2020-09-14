News Classifying Apps
-=-=-=-=-=-=-=-=-=-=-=

##  Requirement
1. Anaconda
2. Keras 2.2.5
3. Flask 1.1.1
4. Tensorflow 1.15.0


##  DISCLAIMER: Pengembangan Aplikasi ini menggunakan OS Windows 10 dengan Python 3.7.7 dan Keras 1.15.0 . 
Untuk OS lain, python > 3.7.7, 3.8 di atas, tensorflow, atau keras versi di atas, 
mohon disesuaikan dengan versi masing-masing


##  How to use:
1. Setup virtualenv (Sesuaikan dengan python/python3) *
> python -m venv venv
> virtualenv -p python venv 

2. Activate virtualenv *
> venv\Scripts\activate 

3. Install semua requirements/library python (Sesuaikan dengan versi pip: pip/pip3)
> pip install -r requirements.txt

4. Jalankan file 
Untuk proses cleaning sampai training dan testing model ada di direktori lstm-model (Semua tahap tidak perlu dilakukan jika hanya ingin menjalankan aplikasinya saja) *
a) Data Cleaning
> masuk ke folder /prepare-data
> jalankan file 1_clean_duplicate.py
> jalankan file 2_concat_remove_anycols.py
> jalankan file 3_filter_as_intent.py (untuk sumber berita detik) / kompas_intent.py / tempo_intent.py / liputan_intent.py (sesuaikan dengan jenis berita yang ingin Anda tentukan class-nya)
> jalankan file 4_clean_datas.py

b) Model Training/Classification
> masuk ke folder /lstm-model
> jalankan file 1_classification.py

c) Model Testing
> masuk ke folder /lstm-model
> jalankan file 2_testing.py untuk menjalankan live input pada salah satu data
> jalankan file 3_prediting_datas.py untuk melakukan evaluasi model

5. Run Apps
> flask run
> ctrl+shift+r for refresh apps (more optimal / clean cache browser)

Note:
* : optional