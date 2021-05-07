#ifndef BRAWLSTARS_CALC_H
#define BRAWLSTARS_CALC_H

#include <stdbool.h>

/* power point constant(s) */
#define PWR_PTS_LVL_1 0
#define PWR_PTS_LVL_2 20
#define PWR_PTS_LVL_3 30
#define PWR_PTS_LVL_4 50
#define PWR_PTS_LVL_5 80
#define PWR_PTS_LVL_6 130
#define PWR_PTS_LVL_7 210
#define PWR_PTS_LVL_8 340
#define PWR_PTS_LVL_9 550
#define PWR_PTS_LVL_10 0

/* coin constant(s) */
#define COINS_LVL_1 0
#define COINS_LVL_2 20
#define COINS_LVL_3 35
#define COINS_LVL_4 75
#define COINS_LVL_5 140
#define COINS_LVL_6 290
#define COINS_LVL_7 480
#define COINS_LVL_8 800
#define COINS_LVL_9 1250
#define COINS_LVL_10 0

/* structure definition(s) */
struct brawler_t {
  // attribute(s)
  char name[16];
  int power_level;
  int star_powers;
  int power_points;
};

struct node {
  // data
  struct brawler_t * brawler;

  // link(s)
  struct node * next;
};

/* forward declaration(s) */
struct node * createList(struct node *, struct brawler_t);
struct node * appendNode(struct node *, struct brawler_t);
struct node * removeNode(struct node *, struct brawler_t *);
struct node * findBrawler(struct node *, const char []);
struct brawler_t * createBrawler(struct brawler_t);
struct brawler_t collectBrawlerInfo(void);
int sumBrawlers(struct node *, int (* ) (struct brawler_t *));
bool reallocateMem(struct node * iter);
void readLine(char []);
void parseBrawler(char *, char *, char *, char *, char *);
void printBrawler(struct brawler_t *);
void printBrawlers(struct node *, void (* ) (struct brawler_t *));
void printMenu(void);
bool writeBrawlers(struct node *);
struct node * readBrawlers(struct node *);
#endif
