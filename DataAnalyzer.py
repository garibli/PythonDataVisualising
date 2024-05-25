# Kütüpaneleri dahil ediniz
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#datasete erişme
df = pd.read_csv('dataset.csv', encoding='latin1')

#Verisetinin ilk satırlarını al ve göster
print("Veri Başlığı")
print(df.head())

#değer girilmeyen haneleri aşkarla
print("\nMissing values in each column:")
print(df.isnull().sum())

#datasetin istatistiklerini göster 
print("\nSummary statistics:")
print(df.describe())

#veri grupları oluşturalım (görselleştirmede kullanmak için)
grouped_df = df.groupby(['District Name', 'Age'])[['Immigrants', 'Emigrants']].sum().reset_index()

# Plotting with Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=grouped_df, x='District Name', y='Immigrants', hue='Age')
plt.title('Total Immigrants by District')
plt.ylabel('Number of Immigrants')
plt.xlabel('District Name')
plt.legend(title='Age Group')
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=grouped_df, x='District Name', y='Emigrants', hue='Age')
plt.title('Total Emigrants by District')
plt.ylabel('Number of Emigrants')
plt.xlabel('District Name')
plt.legend(title='Age Group')
plt.show()

# Combined plot for Immigrants and Emigrants
grouped_df_melted = grouped_df.melt(id_vars=['District Name', 'Age'], value_vars=['Immigrants', 'Emigrants'], 
                                    var_name='Migration Type', value_name='Count')
print(grouped_df_melted)

plt.figure(figsize=(14, 7))
sns.barplot(data=grouped_df_melted, x='District Name', y='Count', hue='Migration Type') #seaborn kütüpanesi
plt.title('Total Immigrants and Emigrants by District')
plt.ylabel('Count')
plt.xlabel('District Name')
plt.legend(title='Migration Type')
plt.show()