# python使用方法
## 端口默认8080
```
url = "http://ip地址:端口/ocr"

# 设置请求头
headers = {
    "Content-Type": "application/json"
}

# 设置请求体数据
data = {
    "image": "iVBORw0KGgoAAAANSUhEUgAAAPoAAAA%2BCAMAAAA1S%2FatAAAAh1BMVEXz%2B%2F4WWFHMq5mpxrjP2%2BHVwM%2FG1Zai1si0rdae0b%2Fgrpzh0KW70tJNgHxolZExbGbX5uiEqaegvb14jaSMl7RlgpMpYmGgosVRd4KUjX97g3YnZ16NwbF8sqNalIielocsYlq1oJBxgXVad2y3ys9EeHWgur1biYeJqas6c2pfj4RxnJGEqp7no8LlAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAGxUlEQVRogc2bC3vbJhSGhWzLlwgJlK7Llnbpuq5btv3%2F37fDTYCAA0KK0%2B9pXddGwMu5cJHcNK5uoKZID0plhdM6HtXfuK5X%2BHMtrSldT0xdt%2FignNy%2BblEO%2FSr5vUZrKipQsdVlL3awOm4sRT2zI82pSjawC%2B5idujIj4NeJwJS7xR1qc87ul6LQzIQZqkI%2Bj74JtAJsfRVkn2rZs9V7KFb8vN5S81dp%2BgJ2Ux%2FJ3TH5ij64WBfnYsjHkPIJvrrdYvHl6t8Ng3RdV4OixKygX5hm7eT6%2FDntVY3NcRUTa9D%2FS7oLjtSMoHukfvXV9JLb78T%2Btz99eiLcAmu3xj2m3SQKiyMZ3hRTViXlyVj178XfCpA48pMboIbj%2FXE9e9CL3t6LN2GxNFlJkxPAwXozU6T%2FTqBpY7HQ9FS%2FCwVfv6QWvGFkxvqNfeHB2jtpWzgfUUFDw9tk2LPpTlXt9sepi%2FeEwC0Re8JGSoaS6MHwtBhA9vt4Pfl2yHp7zo1TYTwisZWoCMSe3exxu%2Fu6fcyzMULJ2QqvWhi81uJ3m5EB2MJqzdil7MFvvjIS8lk%2BIGQ0liH2CCjTg0Cvd2Irk4tNPqmjFex%2FwfRcnRugnKAK1pQTXtWsr8OelO%2Fra9DHwlh%2BVJSMEqcTRz%2BIZTtga7UuUeXdaavQ4d25Oz%2B7Vu26KgdhEGQkJe2eD2ISZB33qHtSniuaqlomkH4Qsz3f%2BanOChqHASmhS%2B%2FA%2FpGuzem06eT%2BX9P1y1wOThgJTqkLgop7zuMQK7o5JSBDn4V6JvZb7eTSy78aRzL4aFPZFJxkyzTc0rpwIOwViua43HMZ7vBWfxAk6%2B7OLzgtuQwogN0kfFCeDHnZLx1mgeSLgAncS1Mc3%2FlVzajswL4B2oq3%2FdeQOlvLfk0gwhnzMOzUfgsWkLWMnCVnP0FDIwvF%2FP791wlbqg3h1cxUmusnmZ3rD7aiBpEYxl4QT6i05MoYUzK%2BKIsNPG3zPBQBoICqaZ30P%2BV73dx%2BJON9cnx3kdCHhtvor8EvkNJZmJOjY1KDPOKRvkXEu8y%2FkbK%2B36iaiz3QFfU6hXMQPnU99DZywdCfpKgBl5ie%2BwD3t9GMj1%2FipxiK3S1oukHmQwGbDVP3dz7%2Bl%2FsXGqj7LxGPn4Eq2tO9UkQMJP1ZbkXCFM8n23uoZsJQVwvmxxz%2BVSOsZx2ec8S51JpYXnOSOR3PlCqB9haNBbzbnK%2FRe9h9uqyEZbd6ib6zC%2BLMp33Ydaj%2BBau143zXGqJCM%2Fws%2Bx2gv38YZrcVgJ40fE5M8XvYSqLinF8%2Ftx4d9HnWKeqEY5Pkdw0NWTngloNxoMvYUpbuL2fwKLozMxm0zMhn727N6pkPzlFsQUdNf1i2exSK24HNeIlF9fyVM7WnA8gSn%2BJoc%2BmvH4a9TD56I5G1JPtcm%2BoO9LKyxnUeIDM8APx9GsM3YQP8OqTKM%2FhvdI9FsL%2B3iW73s%2Bo65zdmreC16Ofyg0KVcyzk4pkUMLqupeCl0l3ctJ8%2BaNMjcfLcnNBVhJ7ZrfojZ4%2FWP%2F4lLKDNvQAboilnLZV0SN5ZSxX37BzvXynYDfsDro9CEJmG12Aor7noYsdQUheeg%2FG3bvQukPchVyr22U844N04iE5uGxeV2G%2B17bU2xD8FiEvfByKOsvlp2ye82ii8mL95Js%2B25ORZdnbFkL0Rb0XS5JgPasfBStq0pohn%2BdKaBaxXswOVhddycC3bTuKk6RGkYdeWvf8m7uHi6uIRrK37Vr0hikjTKjbQ70iMr5O00CWazB5tgToKx%2F7lHp6zCxl3xRda9ITXBxe4DEz%2FQ%2Fhd4p7PXt2RZ6hcSa3evReunEKXp0avvxBIxnTWL2pYN%2BK7ixpJHqLFk6IaWvG%2FV7eJUicmsqv1qOHJwYxlRsS6yIuNodwDL5tm%2BQ9Evnd%2Buecy9Abr09YEdW9KnZ3nimY6d02TbQnyaMPG0X2k0GX5o68KXrfhzv6Ivr8PTOJXX4SswS2b%2FFu2NeNIhh9q2TaLGkwhx6YOMKOXb8jeoPRuy3k08sBebwubeLIh1gj%2B6KnH8ZcoqNNxp%2Buy5o4%2BPDuitJjGT%2BQDnUH3YXKsb%2BvHHrdFckd%2FAIppYN34GzIcPZdtMsPMFx606%2BuWxtYM6B81wXEO3TU014%2FvSFkwb8K3YEM2X8kJVaOJFBBXWRBrV67SuY1P6DBnr1NTjnpRXNI7w2CvXAZwS674O7Kc4WrVb8dSqGrx3Utu1hWmpUlvl9I4ntDgbIL7ndDP5%2BB2mEX1BcHHTsS67oC%2FBS7un4LejE%2BluYsuoK26OiRWOc%2Fk1nM7lxfhf4%2FmnA9FU3EikgAAAAASUVORK5CYII%3D",
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```
